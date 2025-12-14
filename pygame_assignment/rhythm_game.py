import pygame
import random
import os
import sys


#기본 설정
W, H = 800, 600
FPS = 60

LANE_KEYS = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
LANE_LABELS = ["A", "S", "D", "F"]
LANE_X = [220, 320, 420, 520]   #레인 x 좌표
HIT_Y = 520                     #판정선 y 좌표

NOTE_W, NOTE_H = 60, 18

SPAWN_MIN_MS = 380
SPAWN_MAX_MS = 720

#판정 범위
PERFECT_PX = 20
GOOD_PX = 45

AUTO_MISS_PX = 55

MISS_LIMIT = 8
TIME_LIMIT_SEC = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def asset_path(name: str) -> str:
    return os.path.join(BASE_DIR, name)

def try_load_sound(path: str):
    try:
        return pygame.mixer.Sound(path)
    except Exception:
        return None

def try_play_bgm(path: str, volume: float = 0.5):
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        return True
    except Exception:
        return False


#Note 클래스
class Note:
    def __init__(self, lane: int, y: float, speed: float):
        self.lane = lane
        self.x = LANE_X[lane] - NOTE_W // 2
        self.y = y
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(self.x, int(self.y), NOTE_W, NOTE_H)



#해당 레인의 "판정선에 가장 가까운 노트" 찾기
def get_closest_note_index(notes, lane: int):
    candidates = [(i, abs(notes[i].y - HIT_Y)) for i in range(len(notes)) if notes[i].lane == lane]
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[1])
    return candidates[0][0]


#메인
def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("4-Key Rhythm Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 32)
    big_font = pygame.font.Font(None, 64)

    #사운드 파일
    bgm_ok = try_play_bgm(asset_path("bgm.mp3")) or try_play_bgm(asset_path("bgm.wav"))
    sfx_hit = try_load_sound(asset_path("hit.wav"))
    sfx_miss = try_load_sound(asset_path("miss.wav"))

    #색상(판정선 피드백용)
    COLOR_DEFAULT_LINE = (200, 200, 200)
    COLOR_PERFECT = (150, 255, 150)
    COLOR_GOOD = (255, 220, 120)
    COLOR_MISS = (255, 120, 120)

    #게임 상태 초기화 함수
    def reset_game():
        state = {}
        state["notes"] = []
        state["score"] = 0
        state["combo"] = 0
        state["max_combo"] = 0

        state["miss"] = 0
        state["perfect_cnt"] = 0
        state["good_cnt"] = 0
        state["miss_cnt"] = 0

        state["note_speed"] = 3.0
        state["spawn_timer"] = 0
        state["next_spawn_ms"] = random.randint(SPAWN_MIN_MS, SPAWN_MAX_MS)

        state["game_over"] = False
        state["game_started"] = False

        #시작 후 카운트다운
        state["countdown_ms"] = 1200
        state["countdown_left"] = state["countdown_ms"]

        #제한시간은 "시작 버튼 누른 시점"부터
        state["start_ticks"] = pygame.time.get_ticks()

        #판정 텍스트
        state["judge_text"] = ""
        state["judge_left_ms"] = 0

        #판정선 색 피드백
        state["line_flash_color"] = COLOR_DEFAULT_LINE
        state["line_flash_left_ms"] = 0

        #결과 화면에서 이유 표시
        state["end_reason"] = ""
        return state

    st = reset_game()

    while True:
        dt = clock.tick(FPS)

        #이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #R 누르면 재시작
                if event.key == pygame.K_r:
                    try_play_bgm(asset_path("bgm.mp3")) or try_play_bgm(asset_path("bgm.wav"))
                    st = reset_game()
                    continue

                #시작 화면에서 아무 키나 누르면 시작
                if (not st["game_started"]) and (not st["game_over"]):
                    st["game_started"] = True
                    st["countdown_left"] = st["countdown_ms"]
                    st["start_ticks"] = pygame.time.get_ticks()
                    continue

                #게임 진행 중에만 판정
                if (not st["game_over"]) and st["game_started"] and (event.key in LANE_KEYS):
                    lane = LANE_KEYS.index(event.key)
                    idx = get_closest_note_index(st["notes"], lane)

                    if idx is None:
                        # 누를 노트가 없음 = Miss
                        st["miss"] += 1
                        st["miss_cnt"] += 1
                        st["combo"] = 0

                        st["judge_text"] = "MISS"
                        st["judge_left_ms"] = 300
                        st["line_flash_color"] = COLOR_MISS
                        st["line_flash_left_ms"] = 140

                        if sfx_miss:
                            sfx_miss.play()
                    else:
                        dist = abs(st["notes"][idx].y - HIT_Y)

                        if dist <= PERFECT_PX:
                            st["score"] += 150 + st["combo"] * 3
                            st["combo"] += 1
                            st["max_combo"] = max(st["max_combo"], st["combo"])
                            st["perfect_cnt"] += 1

                            st["judge_text"] = "PERFECT"
                            st["judge_left_ms"] = 260
                            st["line_flash_color"] = COLOR_PERFECT
                            st["line_flash_left_ms"] = 120

                            if sfx_hit:
                                sfx_hit.play()
                            st["notes"].pop(idx)

                            #난이도 상승(콤보 10마다 속도 증가)
                            if st["combo"] % 10 == 0:
                                st["note_speed"] += 0.5

                        elif dist <= GOOD_PX:
                            st["score"] += 80
                            st["good_cnt"] += 1
                            st["combo"] = 0  #Good는 콤보 끊기

                            st["judge_text"] = "GOOD"
                            st["judge_left_ms"] = 220
                            st["line_flash_color"] = COLOR_GOOD
                            st["line_flash_left_ms"] = 120

                            if sfx_hit:
                                sfx_hit.play()
                            st["notes"].pop(idx)

                        else:
                            st["miss"] += 1
                            st["miss_cnt"] += 1
                            st["combo"] = 0

                            st["judge_text"] = "MISS"
                            st["judge_left_ms"] = 300
                            st["line_flash_color"] = COLOR_MISS
                            st["line_flash_left_ms"] = 140

                            if sfx_miss:
                                sfx_miss.play()

        #업데이트
        if (not st["game_over"]) and st["game_started"]:
            # 카운트다운 중에는 노트 생성/이동 정지
            if st["countdown_left"] > 0:
                st["countdown_left"] -= dt
            else:
                # 노트 스폰
                st["spawn_timer"] += dt
                if st["spawn_timer"] >= st["next_spawn_ms"]:
                    st["spawn_timer"] = 0
                    st["next_spawn_ms"] = random.randint(SPAWN_MIN_MS, SPAWN_MAX_MS)

                    lane = random.randint(0, 3)
                    st["notes"].append(Note(lane=lane, y=-30, speed=st["note_speed"]))

                # 노트 이동 + 자동 미스 처리
                i = 0
                while i < len(st["notes"]):
                    st["notes"][i].y += st["notes"][i].speed
                    if st["notes"][i].y > HIT_Y + AUTO_MISS_PX:
                        st["notes"].pop(i)
                        st["miss"] += 1
                        st["miss_cnt"] += 1
                        st["combo"] = 0

                        st["judge_text"] = "MISS"
                        st["judge_left_ms"] = 300
                        st["line_flash_color"] = COLOR_MISS
                        st["line_flash_left_ms"] = 140

                        if sfx_miss:
                            sfx_miss.play()
                        continue
                    i += 1

                #게임 오버 조건
                if st["miss"] >= MISS_LIMIT:
                    st["game_over"] = True
                    st["end_reason"] = "Miss limit reached"
                    pygame.mixer.music.stop()

                #제한 시간 체크
                if TIME_LIMIT_SEC is not None:
                    elapsed = (pygame.time.get_ticks() - st["start_ticks"]) / 1000.0
                    if elapsed >= TIME_LIMIT_SEC:
                        st["game_over"] = True
                        st["end_reason"] = "Time up"
                        pygame.mixer.music.stop()

        #판정 텍스트 표시 시간 감소
        if st["judge_left_ms"] > 0:
            st["judge_left_ms"] -= dt
            if st["judge_left_ms"] <= 0:
                st["judge_text"] = ""

        #판정선 색 피드백 시간 감소
        if st["line_flash_left_ms"] > 0:
            st["line_flash_left_ms"] -= dt
            if st["line_flash_left_ms"] <= 0:
                st["line_flash_color"] = COLOR_DEFAULT_LINE

        #그리기
        screen.fill((15, 15, 20))

        #레인
        for x_center, label in zip(LANE_X, LANE_LABELS):
            lane_rect = pygame.Rect(x_center - 50, 0, 100, H)
            pygame.draw.rect(screen, (25, 25, 35), lane_rect)
            pygame.draw.rect(screen, (40, 40, 55), lane_rect, 2)

            txt = font.render(label, True, (220, 220, 220))
            screen.blit(txt, txt.get_rect(center=(x_center, 30)))

        #판정선
        pygame.draw.line(screen, st["line_flash_color"], (0, HIT_Y), (W, HIT_Y), 4)

        #노트
        for n in st["notes"]:
            pygame.draw.rect(screen, (90, 180, 255), n.get_rect(), border_radius=6)

        #UI
        ui1 = font.render(f"Score: {st['score']}", True, (230, 230, 230))
        ui2 = font.render(f"Combo: {st['combo']}  (Max: {st['max_combo']})", True, (230, 230, 230))
        ui3 = font.render(f"Miss: {st['miss']}/{MISS_LIMIT}", True, (230, 230, 230))
        ui4 = font.render(f"Speed: {st['note_speed']:.1f}", True, (230, 230, 230))
        screen.blit(ui1, (20, 20))
        screen.blit(ui2, (20, 50))
        screen.blit(ui3, (20, 80))
        screen.blit(ui4, (20, 110))

        if TIME_LIMIT_SEC is not None and st["game_started"]:
            elapsed = (pygame.time.get_ticks() - st["start_ticks"]) / 1000.0
            remain = max(0, int(TIME_LIMIT_SEC - elapsed))
            ui_t = font.render(f"Time: {remain}s", True, (230, 230, 230))
            screen.blit(ui_t, (20, 140))

        #시작 화면
        if (not st["game_started"]) and (not st["game_over"]):
            msg = big_font.render("RHYTHM GAME", True, (235, 235, 235))
            sub = font.render("Press any key to start", True, (190, 190, 190))
            tip = font.render("A S D F : hit notes | R : restart", True, (160, 160, 160))
            screen.blit(msg, msg.get_rect(center=(W // 2, H // 2 - 40)))
            screen.blit(sub, sub.get_rect(center=(W // 2, H // 2 + 10)))
            screen.blit(tip, tip.get_rect(center=(W // 2, H // 2 + 45)))

        #카운트다운 표시
        if st["game_started"] and (not st["game_over"]) and st["countdown_left"] > 0:
            sec = int(st["countdown_left"] / 1000) + 1
            cd = big_font.render(str(sec), True, (255, 220, 120))
            screen.blit(cd, cd.get_rect(center=(W // 2, H // 2)))

        #판정 텍스트 표시
        if st["judge_text"]:
            color = COLOR_PERFECT if st["judge_text"] == "PERFECT" else COLOR_GOOD if st["judge_text"] == "GOOD" else COLOR_MISS
            jt = big_font.render(st["judge_text"], True, color)
            screen.blit(jt, jt.get_rect(center=(W // 2, HIT_Y - 80)))

        #결과 화면
        if st["game_over"]:
            title = big_font.render("RESULT", True, (235, 235, 235))
            screen.blit(title, title.get_rect(center=(W // 2, 140)))

            lines = [
                f"Score: {st['score']}",
                f"Max Combo: {st['max_combo']}",
                f"Perfect: {st['perfect_cnt']}",
                f"Good: {st['good_cnt']}",
                f"Miss: {st['miss_cnt']}",
            ]
            if st["end_reason"]:
                lines.append(f"End: {st['end_reason']}")

            y = 210
            for line in lines:
                t = font.render(line, True, (220, 220, 220))
                screen.blit(t, t.get_rect(center=(W // 2, y)))
                y += 32

            sub = font.render("Press R to Restart", True, (200, 200, 200))
            screen.blit(sub, sub.get_rect(center=(W // 2, y + 20)))

        #사운드 안내
        if not bgm_ok:
            hint = font.render("No BGM found (bgm.mp3 or bgm.wav).", True, (140, 140, 140))
            screen.blit(hint, (20, H - 35))

        pygame.display.flip()

if __name__ == "__main__":
    main()
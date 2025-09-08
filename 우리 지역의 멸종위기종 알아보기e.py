endangered_species = {
    "곤충류": {"대모잠자리": 2},
    "조류": {"검은머리물떼": 2, "노랑부리저어새": 2, "저어새": 1},
    "양서류": {"맹꽁이": 2, "금개구리": 2}
}

# 1. 지역 입력
region = input("지역 이름을 입력하세요: ")

if region == "인천 서구":
    print("지원 지역입니다.")
    
    # 2. 생물종 입력
    category = input("생물종을 입력하세요 (곤충류/조류/양서류): ")

    if category in endangered_species:
        print(f"{region}의 {category} 멸종위기종 현황:")

        for name, count in endangered_species[category].items():
            print(f"- {name}: {count}급")
    else:
        print("해당 생물종 정보는 없습니다.")
else:
    print("정보 제공을 지원하지 않는 지역입니다.")
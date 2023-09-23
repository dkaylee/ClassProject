
import pandas as pd
          
# results =[

#           ['한과채', '서울 종로구 인사동10길 13', '채식뷔페', '월~토 11:30 ~ 20:30 · 브레이크타임 월~토 14:30 ~ 17:00', '02-720-2802'], 
#           ['만채우', '서울 종로구 인사동11길 24 서울중앙교회 지하 1층', '채식뷔페', '영업시간 월~금 11:30 ~ 15:00', ''], 
#           ['테스패뉴', '서울 중구 무교로 21 코오롱빌딩 1층', '채식뷔페', '', ''], 
#           ['적수방', '서울 중구 동호로24길 7-6 불광산사 지하2층', '채식뷔페', '영업시간 월~토 11:30 ~ 14:30', '02-2276-0993'], 
#           ['투고샐러드건대중문점', '서울 광진구 능동로13길 34', '채식뷔페', '월~토 11:00 ~ 21:30 · 브레이크타임 월~토 15:00 ~ 16:00', '02-499-6787'], 
#           ['비비샐러드', '서울 영등포구 국회대로70길 22', '채식뷔페', '월~금 07:00 ~ 20:00 · 브레이크타임 월~금 14:00 ~ 16:00', ''], 
#           ['셀럽드샐러드(CELEBDESALAD)', '서울 성동구 왕십리로16가길 20', '채식뷔페', '', '02-497-4142'], 
#           ['집밥', '서울 동대문구 망우로18가길 3 태영빌딩 2층', '채식뷔페', '', '02-455-2511'], 
#           ['프리가 전경련점', '서울 영등포구 여의대로 24 전경련회관 지하1층', '채식뷔페', '매일 11:00 ~ 21:00 · 브레이크타임 월~금 14:00 ~ 17:00', '02-3775-1620'], 
#           ['시골건강채식식당', '서울 중랑구 동일로 917-4', '채식뷔페', '', ''], 
#           ['샐러드로우 역삼점', '서울 강남구 논현로95길 30', '채식뷔페', '', '02-2051-6868'], 
#           ['올리브그린뷔페', '서울 영등포구 문래로 164 SK리더스뷰 2층', '채식뷔페', '', ''], 
#           ['베지그린', '서울 강남구 개포로20길 24-10 1층', '채식뷔페', '매일 14:30 ~ 18:00', '02-577-6316'],
#           ['샐러드랍', '경기 구리시 체육관로161번길 13', '채식뷔페', '매일 10:30 ~ 20:00', '031-558-7800'], 
#           ['샐러드바', '서울 강서구 공항대로 426', '채식뷔페', '', ''],
#           ['싱샐러드', '서울 송파구 송파대로28길 27', '채식뷔페', '', '070-7756-4490'], 
#           ['아메리칸트레이 부천점', '경기 부천시 석천로177번길 11', '채식뷔페', '매일 09:00 ~ 21:00', '032-322-4170'], 
#           ['샐러드보울', '경기 의왕시 덕장로 78', '채식뷔페', '', '031-424-3882'], 
#           ['수샐러드', '경기 고양시 덕양구 화정로 52 세이브존 8층', '채식뷔페', '', ''], 
#           ['에바스팩토리', '경기 안양시 동안구 시민대로 230', '채식뷔페', '', '031-388-7020'], 
#           ['스윗치', '경기 고양시 일산동구 무궁화로141번길 7-17', '채식뷔페', '', '070-8865-0466'], 
#           ['뜰안채채식뷔페', '경기 용인시 기흥구 용구대로2335번길 25', '채식뷔페', '매일 15:00 ~ 18:00', '031-281-5879'], 
#           ['삼시세끼한식뷔페', '인천 남동구 예술로 230', '채식뷔페', '', '032-883-1801'], 
#           ['보타닉키친', '인천 남동구 서창남로 16-34', '채식뷔페', '', '032-466-5637'], 
#           ['샐러투데이X오늘도한잔', '경기 파주시 가람로 6', '채식뷔페', '', '031-945-4695'], 
#           ['뜰안채채식뷔페', '경기 수원시 권선구 칠보로88번길 125', '채식뷔페', '매일 15:00 ~ 18:00', '031-291-5879'], 
#           ['피그팩토리', '경기 수원시 팔달구 경수대로718번길 36', '채식뷔페', '', '031-243-8216'], 
#           ['오를레', '인천 연수구 센트럴로 194', '채식뷔페', '', ''], 
#           ['산들', '충남 천안시 동남구 각원사길 150', '채식뷔페', '매일 11:30 ~ 21:00 · 브레이크타임 매일 15:00 ~ 17:30', '041-558-5500'], 
#           ['빛가람채식뷔페', '충북 충주시 안림로 256', '채식뷔페', '영업시간 매일 11:30 ~ 15:00', '043-842-3333'],
#           ['샐러핏', '충남 천안시 동남구 문암로 43', '채식뷔페', '월,화,수,목,금,일 10:00 ~ 21:00', '041-522-8333'], 
#           ['열명의농부', '충북 충주시 신니면 장고개2길 62-46', '채식뷔페', '매일 11:30 ~ 20:00 · 브레이크타임 매일 15:00 ~ 17:00', '043-848-6262'], 
#           ['운김샐러드카페', '충남 천안시 동남구 청수10길 4-83', '채식뷔페', '', '041-567-9917'], 
#           ['샐러드-다', '강원 원주시 일산로 20', '채식뷔페', '', '033-735-8348'], 
#           ['리퍼브14', '대전 대덕구 오정동 133 56주년기념관 2층', '채식뷔페', '월~금 09:00 ~ 20:00', '0504-1845-0791'], 
#           ['채식부페채식사랑', '대전 서구 둔산로 18', '채식뷔페', '', ''], 
#           ['그린샐러드바', '대전 유성구 엑스포로 488 B 110호', '채식뷔페', '', ''], 
#           ['풀꽃세상채식뷔페', '전북 전주시 완산구 우림로 1036-13', '채식뷔페', '매일 11:30 ~ 21:00 · 브레이크타임 월~금 15:00 ~ 17:00', '063-221-4432'], 
#           ['마치래빗 전주신시가지점', '전북 전주시 완산구 홍산남로 30 1층', '채식뷔페', '월~토 11:00 ~ 21:00 · 브레이크타임 월~토 15:30 ~ 17:30', '063-226-1974'], 
#           ['미쁨채식부페', '전북 완주군 소양면 전진로 907', '채식뷔페', '', '063-245-3789'], 
#           ['수자타', '광주 동구 동산길7번길 3', '채식뷔페', '영업시간 매일 11:30 ~ 16:00', '062-222-1145'], 
#           ['스톡홀름샐러드', '대구 동구 경대로 80', '채식뷔페', '월~금 10:30 ~ 19:00', ''], 
#           ['소쇄원채식뷔페', '전남 담양군 가사문학면 지실길 103', '채식뷔페', '영업시간 화~일 11:30 ~ 15:30', '061-383-5255'], 
#           ['스톡홀름 샐러드', '대구 수성구 동대구로77길 9 1층', '채식뷔페', '월~금 10:30 ~ 19:00', ''], 
#           ['럽샐러드', '경북 칠곡군 석적읍 유학로 20', '채식뷔페', '', '054-976-5803'],
#           ['아사모', '전북 전주시 덕진구 아중로 240', '채식뷔페', '', ''], 
#           ['갓샐러드 인동점', '경북 구미시 인동가산로 9-3 1층 102호', '채식뷔페', '', ''], 
#           ['살림채식뷔페', '광주 남구 서문대로 813 삼육빌딩 1층', '채식뷔페', '', '062-675-3553'], 
#           ['갓샐러드연경점', '대구 북구 연경중앙로3길 7', '채식뷔페', '', '053-982-1701'], 
#           ['피키픽', '대구 수성구 달구벌대로645길 11', '채식뷔페', '', ''], 
#           ['오느른샐러드', '경남 거창군 거창읍 아림로 47-1 1층', '채식뷔페', '', '055-943-5232'], 
#           ['갓샐러드 두류평리점', '대구 서구 국채보상로48길 8', '채식뷔페', '', '053-566-1705'], 
#           ['갓샐러드 영대점', '경북 경산시 압량읍 압독2로2길 21', '채식뷔페', '', '053-811-1705'], 
#           ['남도의향기', '전남 화순군 화순읍 쌍충로 74 하나로마트 2층', '채식뷔페', '', ''], 
#           ['단지', '울산 중구 함월3길 16', '채식뷔페', '월~토 11:30 ~ 21:00', '052-244-2234'], 
#           ['자연채식뷔페신라', '경북 경주시 영불로 217', '채식뷔페', '', '054-772-0014'], 
#           ['오부리또', '경남 창원시 성산구 원이대로473번길 9', '채식뷔페', '', '055-282-1300'], 
#           ['센텀셀러드뷔페', '경북 경주시 알천북로 1', '채식뷔페', '', '054-777-2522'], 
#           ['담은하늘채', '전남 목포시 평화로 38-7', '채식뷔페', '월~토 11:30 ~ 21:00 · 브레이크타임 월~토 15:00 ~ 17:30', '061-284-6277'], 
#           ['샐러드ME', '광주 서구 회재로 1054', '채식뷔페', '', '062-676-8788'],
#           ['샐러드바', '전남 광양시 동광길 29', '채식뷔페', '', ''], 
#           ['오늘샐러드', '경남 진주시 솔밭로91번길 11', '채식뷔페', '', '055-758-3378'], 
#           ['초선재', '울산 남구 화합로71번길 21', '채식뷔페', '월~목 12:00 ~ 20:00 · 브레이크타임 월~목 14:00 ~ 17:30', ''], 
#           ['샐러드장인', '전남 무안군 삼향읍 남악5로46번길 22', '채식뷔페', '', '061-281-9778'], 
#           ['샐럽', '울산 남구 신정로78번길 21', '채식뷔페', '', '052-266-3599'], 
#           ['빵굽는언니 요리하는동생', '부산 강서구 명지국제8로 234 정우빌딩 2층 201호', '채식뷔페', '', '051-292-1357'], 
#           ['힐링키친 울산삼산점', '울산 남구 왕생로62번길 15-1 2층', '채식뷔페', '', '070-4101-6999'], 
#           ['트레인(TRAIN)1095', '경남 양산시 남부10길 1', '채식뷔페', '', '055-382-1006'], 
#           ['슈퍼샐러드', '부산 남구 수영로298번길 39-9', '채식뷔페', '', '051-631-5923'], 
#           ['뱃살도둑 여수점', '전남 여수시 여문2로 128-38', '채식뷔페', '', '061-653-8283'], 
#           ['단물', '경남 통영시 중앙로 109-1', '채식뷔페', '', '055-644-2500'], 
#           ['풀마니 해운대점', '부산 해운대구 대천로 40', '채식뷔페', '', '051-731-0479]'], 
#           ['목수의농장', '제주특별자치도 제주시 애월읍 애상로 207-5', '채식뷔페', '', '064-742-2155'], 
#           ['셰발레리', '서울 마포구 포은로 52 1층', '양식', '월,화,수요일', '02-6013-0269'], 
#           ['비건스페이스', '서울 용산구 신흥로2길 7', '카페', '매일 11:00 ~ 20:00', '']


# ]

# # 크롤링한 결과 results를 pandas의 데이터 폼으로 읽기
# results_df = pd.DataFrame(results)
# results_df.colums = ['mat_title', 'mat_addr', 'mat_cont', 'mat_time', 'mat_num']
# results_df.to_csv('/Users/dkaylee/Documents/GitHub/ClassProject/ClassProject/python/b_matzip.csv', index = False)


results_2 =[
          ['한국채식연합', '서울 마포구 고산16길 49-4', '환경단체', '', '02-707-3590'], 
          ['채식은복이다', '서울 중구 다산로46길 17', '중화요리', '', ''], 
          ['시골건강채식식당', '서울 중랑구 동일로 917-4', '채식뷔페', '', ''], 
          ['뜰안채채식뷔페', '경기 용인시 기흥구 용구대로2335번길 25', '채식뷔페', '영업시간 매일 12:00 ~ 21:00 · 브레이크타임 매일 15:00 ~ 18:00'], 
          ['031-281-5879', '로비건채식요리학원', '서울 서초구 양재천로21길 3', '요리학원', '', ''],
          ['뜰안채채식뷔페', '경기 수원시 권선구 칠보로88번길 125', '채식뷔페', '영업시간 매일 12:00 ~ 21:00 · 브레이크타임 매일 15:00 ~ 18:00', '031-291-5879'], 
          ['한국채식비건협회', '서울 송파구 송파대로 201 B동 606호', '단체,협회', '', '02-2135-1933'], 
          ['채식나라농업회사법인', '경기 하남시 조정대로 45 FB325호', '식품', '', ''], 
          ['채식쿠킹연구소', '경기 포천시 가산면 마전길 237-1', '교육,학문', '', '031-543-4047'], 
          ['채식명가명품주유소', '충남 아산시 영인면 아산로 854', 'S-oil주유소', '', '041-543-5159'], 
          ['빛가람채식뷔페', '충북 충주시 안림로 256', '채식뷔페', '영업시간 매일 11:30 ~ 15:00', '043-842-3333'], 
          ['생명사랑채식수련원', '강원 영월군 무릉도원면 도원운학로 202-33', '교육단체', '', ''], 
          ['채식부페채식사랑', '대전 서구 둔산로 18', '채식뷔페', '', ''], 
          ['풀꽃세상채식뷔페', '전북 전주시 완산구 우림로 1036-13', '채식뷔페', '영업시간 매일 11:30 ~ 21:00 · 브레이크타임 월~금 15:00 ~ 17:00', '063-221-4432'], 
          ['미쁨채식부페', '전북 완주군 소양면 전진로 907', '채식뷔페', '', '063-245-3789'],
          ['소쇄원채식뷔페', '전남 담양군 가사문학면 지실길 103', '채식뷔페', '영업시간 화~일 11:30 ~ 15:30', '061-383-5255'], 
          ['진홍채식이샤브', '대구 달서구 두류공원로 262', '샤브샤브', '', '053-653-6633'], 
          ['살림채식뷔페', '광주 남구 서문대로 813 삼육빌딩 1층', '채식뷔페', '', '062-675-3553'], 
          ['자연생활채식부페', '전북 정읍시 동부1길 74', '뷔페', '', '063-533-2114'], 
          ['금강자연비건채식도시락', '대구 달성군 현풍읍 테크노중앙대로5길 33-19', '도시락', '', ''], 
          ['즐거운채식', '광주 서구 매월2로15번길 16', '식품', '', ''], 
          ['자연채식뷔페신라', '경북 경주시 영불로 217', '채식뷔페', '', '054-772-0014'], 
          ['첫번채식당', '경남 고성군 거류면 거류로 618', '해물,생선', '', '055-672-2450'], 
          ['채식카페 작은부엌', '제주특별자치도 제주시 조천읍 선흘동2길 1', '한식', '영업시간 화~토 10:00 ~ 15:00', '010-4699-3179'], 
          ['경주자연건강 단식채식생활관', '경북 경주시 양북면 범곡리 563', '단식원', '', '054-745-2294'], 
          ['채식식당 푸른솔맑은향', '제주특별자치도 제주시 고사마루길 125', '한식', '영업시간 월,수,목,금,토 11:30 ~ 20:00', '064-749-9935'], 
          ['밥브레드', '경기 고양시 일산동구 일산로380번길 5-20 1층', '제과,베이커리', '영업시간 월~토 09:00 ~ 21:00', '010-5412-5053'], 
          ['알키미아', '경기 고양시 일산동구 일산로463번길 23-16', '아이스크림', '', '010-2355-7672'], 
          ['올리코', '경기 고양시 일산서구 호수로856번길 7-16', '이탈리안', '영업시간 화~금 11:30 ~ 22:00 · 브레이크타임 화~일 15:00 ~ 17:00', '031-913-1324'], 
          ['진저앤트리클', '경기 고양시 일산동구 일산로441번길 41-17', '양식', '영업시간 월,수,목,금,토,일 12:00 ~ 15:00', '010-4104-7514'],
          ['코미치 홍대점', '서울 마포구 와우산로29길 4-13', '일식', '영업시간 매일 11:30 ~ 21:30', '070-4001-1291'], 
          ['펠앤콜 홍대본점', '서울 마포구 와우산로 39-21', '아이스크림', '영업시간 월,화,수,목,금,일 12:00 ~ 21:00', '070-4411-1434'], 
          ['공작', '서울 마포구 희우정로12길 23 동광펠리스 101호', '호프,요리주점', '', '070-8876-0404'], 
          ['샐러디 마곡발산역점', '서울 강서구 공항대로 269-15 힐스테이트에코마곡 1층 104호', '패스트푸드', '영업시간 월~금 08:00 ~ 21:00', '02-2643-9143'], 
          ['사직동그가게', '서울 종로구 사직로9길 18', '카페', '영업시간 화~일 11:30 ~ 20:00', '070-4045-6331'], 
          ['아필립', '서울 마포구 성미산로 191', '술집', '매일 18:00 ~ 05:00', ''], 
          ['쌈잇쌈', '서울 마포구 와우산로15길 28 2층', '동남아음식', '', ''], 
          ['카페라그린', '서울 중구 정동길 26 1층', '카페', '영업시간 월~토 11:00 ~ 20:00', '02-3789-8005'], 
          ['죠티인도레스토랑 신촌점', '서울 마포구 신촌로20길 6', '인도음식', '영업시간 매일 11:30 ~ 22:30', '02-703-3535'], 
          ['올어바웃어스', '서울 마포구 연남로3길 13 2층', '카페', '영업시간 화~일 13:00 ~ 22:00', ''], 
          ['카사블랑카', '서울 용산구 신흥로 35 1층', '샌드위치', '영업시간 화~일 12:00 ~ 22:00', '02-797-8367'], 
          ['박명도봉평메밀막국수 본점', '서울 용산구 원효로 184', '국수', '영업시간 매일 10:00 ~ 22:00', '02-717-7711'], 
          ['빵어니스타 여의도점', '서울 영등포구 국제금융로8길 16 지하1층 B129호', '제과,베이커리', '영업시간 매일 12:00 ~ 20:00', ''], 
          ['한상훈셰프', '서울 중구 소공로 29', '양식', '영업시간 월~토 11:00 ~ 22:00', '02-771-1808'],
          ['더닐크팩토리 가로수길지점', '서울 강남구 강남대로162길 32 나라빌딩 1층', '디저트카페', '영업시간 매일 11:00 ~ 22:00', '02-2039-0821'], 
          ['펭귄키친', '서울 강서구 마곡중앙2로 35 3층 322호', '제과,베이커리', '', ''], 
          ['놉스', '서울 은평구 연서로 455 541동 1층 104호', '제과,베이커리', '영업시간 수~일 10:00 ~ 19:00', '070-8809-9022'], 
          ['대구집', '서울 성동구 살곶이길 40', '육류,고기', '매일 11:30 ~ 02:00', '02-2294-6349'], 
          ['타지 명동점', '서울 중구 명동길 73', '인도음식', '영업시간 매일 12:00 ~ 22:00 · 브레이크타임 월~금 15:00 ~ 17:30', '02-776-0677'], 
          ['그러팡야', '서울 마포구 포은로 48', '제과,베이커리', '', ''], 
          ['에코밥상', '서울 종로구 사직로 127-14', '한식', '영업시간 월~토 11:30 ~ 22:00 · 브레이크타임 월~토 15:00 ~ 17:00', '02-736-9136'], 
          ['공간녹음', '서울 강서구 공항대로 227 403호', '양식', '영업시간 월~토 11:30 ~ 22:00 · 브레이크타임 월~토 15:00 ~ 17:30', '02-6953-6998'], 
          ['샐러디 종로광교점', '서울 종로구 청계천로 61 관철동빌딩 6층', '패스트푸드', '영업시간 월~금 08:00 ~ 21:00', '02-6956-7996'], 
          ['마을찻집 마주이야기', '서울 강북구 인수봉로55길 10 2층', '카페', '영업시간 화~금 14:00 ~ 21:00', '070-8615-6011'], 
          ['아승지', '서울 영등포구 신길로 176', '한식', '영업시간 월~금 12:00 ~ 15:00', '02-836-8442'], 
          ['술탄터키케밥하우스', '서울 용산구 보광로 126', '터키음식', '매일 00:00 ~ 24:00', '02-749-3890'], 
          ['우리동네나무그늘', '서울 마포구 백범로 113-1 2층', '카페', '영업시간 월~금 10:00 ~ 22:30', '02-6408-5775'], 
          ['그러케이크샵', '서울 마포구 희우정로12길 18 1층', '제과,베이커리', '', ''], 
          ['밥먹는술집광장', '서울 중구 수표로 63-1 2층', '호프,요리주점', '영업시간 월~목 13:00 ~ 23:00', ''],
          ['나빈인디안레스토랑', '서울 노원구 노해로 494 3층', '인도음식', '', '02-931-1557'], 
          ['정광균의순수한빵생활', '서울 양천구 목동중앙남로 12 1층', '제과,베이커리', '', '010-6832-7752'], 
          ['이세계는놀이터예요', '서울 서대문구 이화여대길 88-15 1층', '한식', '영업시간 월~금 10:00 ~ 15:00', ''], 
          ['홀리차우 이태원점', '서울 용산구 이태원로 179 해밀톤호텔 2층', '퓨전중식', '영업시간 매일 11:30 ~ 22:00', '02-793-0802'], 
          ['카페기웃기웃', '서울 마포구 신촌로12다길 20 스테이하이오피스텔 1층', '카페', '영업시간 화~일 12:00 ~ 21:00', ''], 
          ['팡도리노베이커리', '서울 중랑구 용마산로115길 127 한일써너스빌리젠시1단지 상가 1005호', '제과,베이커리', '', '070-8822-2738'], 
          ['마히나비건테이블', '서울 강남구 논현로175길 75 2층', '이탈리안', '영업시간 화~일 12:00 ~ 21:30 · 브레이크타임 화~일 16:00 ~ 17:30', '0507-1371-5331'], 
          ['브레드몽드', '서울 관악구 관악로 200 1층', '제과,베이커리', '', '02-887-2720'], 
          ['손오공마라탕 강남점', '서울 강남구 강남대로102길 22 2층', '중화요리', '영업시간 매일 11:00 ~ 23:00', '02-555-5959'], 
          ['일용할양식', '인천 남동구 인주대로522번길 50', '양식', '영업시간 월~토 11:00 ~ 21:00 · 브레이크타임 월~토 15:30 ~ 17:30', '010-7383-3303'], 
          ['비스포킷 광화문 D타워점', '서울 종로구 종로3길 17 D타워 1층 102호', '도시락', '', ''], 
          ['알프리베', '서울 관악구 남부순환로188길 9 차일드빌딩 1층', '제과,베이커리', '영업시간 월~토 12:00 ~ 19:00', '02-888-1317'], 
          ['깔리 사당점', '서울 서초구 방배천로 21 동화빌딩 4층', '인도음식', '영업시간 매일 11:30 ~ 22:00', ''], 
          ['더담백', '서울 성북구 화랑로 210-6', '제과,베이커리', '영업시간 수~일 11:00 ~ 20:00', '02-942-0186'], 
          ['알로하포케 논현점', '서울 서초구 강남대로79길 22 2층', '양식', '영업시간 월~금 11:00 ~ 22:00', '02-540-4864']
          ]

# 크롤링한 결과 results를 pandas의 데이터 폼으로 읽기
results_2_df = pd.DataFrame(results_2)
results_2_df.colums = ['mat_title', 'mat_addr', 'mat_cont', 'mat_time', 'mat_num']
results_2_df.to_csv('/Users/dkaylee/Documents/GitHub/ClassProject/ClassProject/python/b_matzip_2.csv', index = False)
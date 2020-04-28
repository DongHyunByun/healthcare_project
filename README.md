# healthcare_project

1. **기간 : 2019.03~2019.06**

2. **기술스택 : sklearn, numpy, graphviz**

3. **내용 : 당뇨, 고혈압, 이상지질혈증의 지역별 발병률을 통해 어떠한 요인이 해당 질병들의 발병에 영향을 미치는지 탐색적 분석.**

    1. 지역을 254개의 시,군,구 단위로 나누어 각각을 하나의 record로 봄.
    2. 속성을 총 4개(a.총건강결과, b.건강행태, c.물리적 환경, d.보건의료체계)의 대분류로 나누고, 아래와 같이 15경우로 조합하여 유병률과의 상관관계를 파악
        - 1개 조합 (a,b,c,d) => 4가지
        - 2개 조합 (ab,ac,ad,bc,bd,cd) => 6가지
        - 3개 조합 (abc,abd,acd,bcd) => 4가지
        - 4개 조합 (abcd) => 1가지
    3. 각 조합별 당뇨, 이상지질혈증, 고혈압의 유병률을 class로 하는 의사결정나무를 이용하여 높은 accuracy값을 갖는 속성의 조합을 찾음.
  
4. **파일설명**  
    1. 1 전처리
        - add_3att.py : class att(고혈압, 당뇨, 이상지질혈증의 유병률(표준화))를 추가
        - delete_null_location.py : 지역코드가 없는 지역을 제외
        - make_null_average.py : 결측치를 평균값으로 대체
        ![결측치 평균값](https://user-images.githubusercontent.com/50386280/80488073-c3215f80-8998-11ea-9890-bd8481771c46.jpg)
        - sum_all_one(add chs).py : 년도별 공통지역, 공통속성을 찾음
        ![공통구역](https://user-images.githubusercontent.com/50386280/80488315-18f60780-8999-11ea-85c1-499254ec4d2a.jpg)
    2. 2 tree만들기
        - %.csv : 15개 조합에 대한 전처리된 데이터 (건강결과(Health Outcome), 건강행태(Health Behavior), 물리적환경(Physical Environment), 보건의료체계(Health Care System)) 
        - tree_for_capston.ipynb : 각 조합에 대한 tree 작성
    3. 3 결론
        - tree.folder : 각 속성의 조합(15가지)별 3가지 class att(당뇨, 이상지질혈증, 고혈압의 유병률)에 대한 트리 => 총 45개의 tree
        - compare accuracy.xlsx : 각 tree의 
 

# 2. Network Communities

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled.png)

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%201.png)

- network : 타이트하게 연결된 노드들
- network communities - 내부 연결은 많고 외부 연결은 적은 노드 집합

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%202.png)

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%203.png)

- split 은 가작 적은 수의 edge cut으로 설명될 수 있어야함

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%204.png)

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%205.png)

- 광고 등에서 공통 관심사 공통키워드 등
- 도박이랑 스포츠 베팅하는 무리랑 비슷한 클러스터링되어있음

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%206.png)

- 이렇게만 봤을 때는 어떻게 클러스터링을 해야할지 감이 안옴

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%207.png)

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%208.png)

- 이것을 어떻게 공식화할 수 있을까?
- communities : 타이트하게 연결된 노드 집합
- Modularity Q : 커뮤니티 내부에서 얼마나 잘 분리되어있는지 측정치
→ Sum[그룹내부 노드가 가진 모든 엣지 수(외부 엣지는 미포함) - 예상되는 그룹 내부 엣지 수(null model로 예측할 수 있음)]

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%209.png)

- Null Model : Configuration Model
→ n개의 node 와 m 개의 edge를 **랜덤으로 재연결**
→ 같은 정도(거리) 분리 되었음, 균일하게 랜덤 연결을 진행
→ 이때 멀티그래프 (즉, 노드간의 여러개의 연결 가능)
    
    
- k_i : i에 연결된 link 수

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%2010.png)

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%2011.png)

- 즉 Null model에서 엣지는 보존되며, 예상되는 엣지 수 는(multigraph 일지라도) m 개임

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%2012.png)

- 여기서 A_ij 는 i→j 일 경우 1로 보니까 A_ji = 1 로 볼 수 있음
→ 1개의 edge를 두번 카운트 한다는 것을 알 수 있음.
- 앞의 2m 은 정규화하기 위한 수
→ 약 0.7 이상이 나오면 충분히 커뮤니티 구조라고 할 수 있음

![Untitled](2%20Network%20Communities%201a6b476e159b4d03ab30f850855eee6d/Untitled%2013.png)

- Modularity Q를 최대화하면서 커뮤니티를 찾아낼 수 있음
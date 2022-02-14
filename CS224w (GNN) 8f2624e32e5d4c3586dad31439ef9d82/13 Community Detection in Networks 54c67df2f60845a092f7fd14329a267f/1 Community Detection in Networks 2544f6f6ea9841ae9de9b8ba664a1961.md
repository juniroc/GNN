# 1. Community Detection in Networks

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled.png)

- 그래프에서 노드 집합을 클러스터링 하는 것으로 이해할 수 있음

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%201.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%202.png)

- Information flow
    - Short link : 강한 유대관계 (Strong friendships)
    - Long link : 약한 유대관계 (just our acquaintances and kind of colleagues and people we meet less often)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%203.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%204.png)

- Granovetter의 friendship 두가지 관점
    - Structural perspective : 링크가 네트워크의 어떤 부분을 연결하는가 ?
    - Interpersonal perspective : 링크가 Strong or Weak ?

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%205.png)

- First point : Structure
    - 구조적으로 강하게 연결된(tightly-connected) edges는 Socially strong
    - 네트워크의 다른 부분들에 걸쳐있는 edges(Long-range Edges)는 Socially weak
- Second point : Information
    - 구조적으로 연결된 edges는 Information access관점에서 매우 중복(redundant)
    - 다른 network와 연결된 edges(Long-range edges)는 더 많은 정보를 줄것이다. (other community에 접근할 수 있기 때문에)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%206.png)

- a-b 가 a-c 보다 더 연결될 가능성이 높음

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%207.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%208.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%209.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%2010.png)

- data : EU 통화 데이터
- Edge Weight 는 통화 횟수
- Edge Overlap(O_ij) : i,j 의 node neighbors 중 얼마나 많은 지인(nodes)를 공유(overlap)하는지에 대한 정보
- 통화횟수가 많을 수록 O_ij 값이 커졌음
→ Strong Edges 를 가진 Communities 존재
- 즉, 실제 데이터와 Edges 의 관계를 통한 증명

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%2011.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%2012.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%2013.png)

![Untitled](1%20Community%20Detection%20in%20Networks%202544f6f6ea9841ae9de9b8ba664a1961/Untitled%2014.png)
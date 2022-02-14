# 1. Reasoning in Knowledge Graphs

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%201.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%202.png)

- 10 챕터에서 다룬 KG completion 이 1 hop 에 해당하는 지식을 얻어내는 작업이라면, 
→ `이를 n hop으로 확장할 수 있지 않을까?` 라는 관점에서 나옴

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%203.png)

- 지식 그래프를 이용해서 `multi hop`의 지식을 얻어내는 작업을 `reasoning(추론)`

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%204.png)

- One-hop Queries
    - head 와 relation이 주어진 상태에서 tail 예측
    - KG Completion 과 동일한 작업
    - 현재 노드에서 정해진 엣지를 이용할 때 어떤 노드로 이동할지 정하는 작업
    
- Path Queries
    - Fulvestrant 에서 시작하여 n 개의 관계를 지나 도달할 수 있는 노드 추론
    - 출발 노드 = anchor (v_a)
    
- Conjunctive Queries
    - 하나의 anchor entity가 아닌 다수의 anchor 가 각자의 path query를 가지고 그 합성으로 올 수 있는 tail 예측하는 것

### Predictive One-hop Queries

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%205.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%206.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%207.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%208.png)

- 위 그래프를 보면 엣지를 따라가면 만족하는 테스크를 수행할 수 있을 것 같다
→ PIM1 과 CASP8을 얻음
- 그러나 **해당 그래프는 엣지가 (매우 많이) 비어있는 상태**
→ **즉 해당 그래프는 불완전하다.**

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%209.png)

- 엣지가 상당히 비어있음

ex) 

- 인스타나 페북에 프로필 업데이트를 안했을 경우,
- 테슬라 신차 업데이트가 안된 경우
- 우리가 알지 못하는 약 - 질별 관계 등..

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%2010.png)

 

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%2011.png)

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%2012.png)

- 그러면 KG completion을 이용해 그래프를 완성시키고 탐색 알고리즘 실행?
→ 그래프 완성하는 것은 불가능에 가까움
    
    왜? → 모든 쌍은 연결될 가능성이 0이 아님
    

![Untitled](1%20Reasoning%20in%20Knowledge%20Graphs%2043aec111db0644f49a5b13bc762c9abd/Untitled%2013.png)
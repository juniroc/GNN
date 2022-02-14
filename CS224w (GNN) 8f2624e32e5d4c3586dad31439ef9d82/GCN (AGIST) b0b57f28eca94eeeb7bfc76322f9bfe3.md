# GCN (AGIST)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled.png)

4개의 Node / 5개의 Feature

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%201.png)

- 노드 feature 값을 업데이트하고 싶음.

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%202.png)

- X = H^(0) 라고 생각하면 됨
→ X 는 초기 feature Matrix

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%203.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%204.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%205.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%206.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%207.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%208.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%209.png)

- 여기를 보면 Adjacency Matrix는 변함없지만,
- Feature Matrix 는 변화가 생김 (업데이트가 됨)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2010.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2011.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2012.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2013.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2014.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2015.png)

- 어떤 `Feature Matrix` 인지는 도메인에 따라 다르다
→ 본인이 `feature`를 어떻게 지정하느냐에 따라 바뀜 (원핫으로 길게 펼칠 수 있음)
ex) 화학식의 경우, 원소에 따른 원핫 등 f가 길어질 수 있음
- `Weight Matrix` → `CNN`의 필터수 정도로 이해하면 됨
- 단, `CNN`에서는 인풋 이미지(인풋데이터)가 1개 이지만,
`GCN`에서는 인풋 노드(인풋데이터 1개)와 인접 데이터(인풋데이터 1개) 총 인풋데이터 2개가 필요로 함.

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2016.png)

- 노드 순서에 따라 값이 바뀌는 경우를 대비해서
→ Node-wise Summation 기법을 이용
→ i번째 노드의 H(idden) state를 모두 더해버리는 기법
- 제일 쉬운 방법임

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2017.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2018.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2019.png)

![Untitled](GCN%20(AGIST)%20b0b57f28eca94eeeb7bfc76322f9bfe3/Untitled%2020.png)
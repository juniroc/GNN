# 2. Neural Subgraph Matching

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled.png)

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%201.png)

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%202.png)

- 해당 Query 그래프가 Target 그래프의 subgraph 인가?

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%203.png)

- 이를 판단하기 위해 embedding space의 기하 모형(geometric shape)을 활용
- 이 embedding space 를 구하기 위해 GNN을 이용

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%204.png)

- 이진 예측으로 subgraph 이면 True 아니면 False

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%205.png)

- Query graph와 Target graph가 있을때 각각 No 또는 Yes 로 구분(이진 분류)하기위해 학습

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%206.png)

- 노드 고정 (노드 앵커) 및 앵커 노드 임베딩 작업

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%207.png)

- 앵커 노드의 이웃 노드에 대해 임베딩

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%208.png)

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%209.png)

- 앵커가 기준이 되어, 이웃 임베딩 생성

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2010.png)

- 이웃 노드 분해는 어떻게?
→ BFS 등으로 k-hop 이웃을 얻음

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2011.png)

- 순서 임베딩 공간에 대한 개념

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2012.png)

- 왼쪽 아래가 중요한 이유
→ 하위 관계로 볼 수 있기 때문

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2013.png)

- 순서 임베딩 공간
    - 서브 동형 관계가 순서 임베딩 공간에 나타내 질 수 있음

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2014.png)

- Transitivity
    - 노란색은 초록색의 subgraph
    - 초록색은 빨간색의 subgraph
    → 동시에 노란색은 빨간색의 subgraph
- Anti-symmetry
    - 노란색 == 초록색 같은 graph
- Closure under intersection
    - 노란색이 초록색과 빨간색의 부분 subgraph

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2015.png)

- 순서 임베딩구조를 학습하기 위해서 적절한 loss function을 구축해야함
→ 그게 바로 `**Max-margin** loss function`

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2016.png)

- max-margin loss 라는 공식을 이용해 해당 subgraph가 순서 임베딩 공간에 표현되도록 학습

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2017.png)

- 여기서 G_q 는 G_t의 Subgraph 인지 판한다는 그래프, 만약 E(G_q, G_t) > 0 이면 Subgraph가 아니다.
→ 위 그림을 통해 확인할 수 있음

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2018.png)

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2019.png)

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2020.png)

- BFS sampling 중 각 스텝의 10% 만을 통해 Subgraph (G_q)를 만들고
→ Positive Example
- 반대로 생성된 G_q 에서 노드 추가 생성 및 제거를 통해 가짜 예시를 만든다
→ Negative Example

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2021.png)

- 데이터 셋에 따라 BFS Sampling 깊이를 조정
→ 보통 3-5 정도로 함

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2022.png)

- 새로운 그래프가 주어졌을 때, 이것이 G_t 의 subgraph인지 판단 하는 방법
→ G_q의 Embedding 공간이 G_t Embedding 공간에 포함하는지 판단하면 됨.

![Untitled](2%20Neural%20Subgraph%20Matching%20e40e79c684c74343afa3715de832c033/Untitled%2023.png)
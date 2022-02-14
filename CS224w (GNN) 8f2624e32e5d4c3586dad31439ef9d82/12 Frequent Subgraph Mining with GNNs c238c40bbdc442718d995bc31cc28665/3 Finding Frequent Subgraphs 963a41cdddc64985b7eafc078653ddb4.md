# 3. Finding Frequent Subgraphs

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%201.png)

- 가장 빈번한 motif를 찾기 위해서는 위 두가지가 해결되어야 함
    1. 열거 가능
    2. 카운팅 가능
- 위 그림에서보면 삼각형 subgraph 구조는 3개가 있는걸 확인할 수 있음

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%202.png)

- subgraph 존재를 확인하는 것은 상당히 많은 코스트가 듦

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%203.png)

- 계산적으로 기하급수적으로 증가하기에 어려움이 있는데
→ Representation learning은 이러한 문제를 해결하는데 도움을 줌

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%204.png)

- Counting
→ GNN 을 이용해서 빈도 예측
- Enumerating
→ 열거하지말고 k 사이즈를 가지는 subgraph를 구축

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%205.png)

- 그러나 이런 방법은 많은 cost를 요구하기 때문에 어려움이 있음
→ 그래서 Representational learning 으로 해결할 수 있음

## SPMiner

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%206.png)

- G_t 그래프를 임베딩 공간에 나타낸 뒤에 주어진 Subgraph(G_q) 를 모두 비교하며 빈도 수를 구하는 것

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%207.png)

- Key Idea
→ G_t 를 이웃으로(subgraph)로 쪼개는 것

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%208.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%209.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2010.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2011.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2012.png)

 

- K-step 마다 가장 많은 neighborhood embedding 을 포함하는 Motif찾는 것이 목표
- 학습은 무작위로 한개의 노드를 초기의 값으로 선택한 후, 각 step 마다의 subgraph를 저장하는 과정
- 지정한 k에 도달하면 학습 멈춤

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2013.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2014.png)

![Untitled](3%20Finding%20Frequent%20Subgraphs%20963a41cdddc64985b7eafc078653ddb4/Untitled%2015.png)
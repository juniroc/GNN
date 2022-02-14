# 1. Heterogeneous Graphs and Knowledge Graph Embeddings

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%201.png)

**Homogeneous / Heterogeneous Graph**

`Homogeneous graph` 는 그래프의 **모든 노드가 같은 성질을 갖고 있는 그래프**이다. 예를 들어, **인물 관계도**가 있다면 **모든 노드는 사람을 의미**하는 homogeneity를 갖는다.

`Heterogeneous graph` 는 반대로 **그래프의 노드가 여러 종류의 성질을 가지는 그래프**이다. 예를 들어 **영화-유저 그래프는 어떤 노드는 영화**이고, **어떤 노드는 유저**를 의미하는 heterogeneity를 갖는다.

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%202.png)

- 이질적 그래프는 위와 같이 4가지 파라미터를 가진 것으로 표현 가능

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%203.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%204.png)

- 이질 그래프는 GCN을 확장하여 다룸

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%205.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%206.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%207.png)

- 멀티플 관계가 있는 경우?

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%208.png)

- 다른 `Neural Network Weight`를 이용한다

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%209.png)

- 다음과 같이 이용될 수 있음.

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2010.png)

- Relational GCN (RGCN)
- W_r* h_u 가 각 관계별 W곱

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2011.png)

- 최적화 방법 2가지(계산을 줄이는 방법 or 확장하는 방법)
- 대각행렬곱

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2012.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2013.png)

- dictionary learning

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2014.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2015.png)

- Category를 4개로 나누어 학습 및 예측 진행
- 핵심은 각 관계 유형에서 독립적으로 변환 후 병합하는 것

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2016.png)

**예시**

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2017.png)

- Training supervision edges를 하나 정하면
→ 나머지 (Training message edges)를 이용해 Training supervision edges 를 예측
- 이때 negative edge 를 생성하여 꼬리를 방해함
→ Negative edges는 training message edges 나 training supervision edges 에 포함되지 않은 것

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2018.png)

- training supervision edge 와 negative edges를 이용해 loss function을 구함 (sigmoid function)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2019.png)

- Validation edges 는 Training message edges 와 training supervision edges를 이용해 예측
→ 이때 validation edges는 Training message edges 와 Training supervision edges에 포함되지 않은 edges보다 스코어가 높아야함
    
    → 왜?? : (확실치 않지만) negative edges 이면 말이 됨.
    - negative edges는 학습하는 과정에서 loss를 오히려 올리는 방향으로 학습되었으니 스코어가 낮을 수 밖에 없음
    

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2020.png)

![Untitled](1%20Heterogeneous%20Graphs%20and%20Knowledge%20Graph%20Embeddi%20a3e826a4866f4fe499d5ddacea9097f6/Untitled%2021.png)
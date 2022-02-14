# 2.  Training Graph Neural Networks

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%201.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%202.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%203.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%204.png)

- prediction Heads 중에서도 레벨별로 다른 예측 태스크를 갖음

### Node-level

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%205.png)

- 그래프 내 모든 노드 임베딩을 직접사용하여 예측

### Edge-level

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%206.png)

- 그래프 내 예측하고하자는 edge와 연결된 node 쌍을 이용해 예측

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%207.png)

- node 쌍을 concat하여 linear 예측

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%208.png)

- node쌍의 임베딩 간 내적을 통해 예측

### Graph-level

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%209.png)

- 모든 node 의 임베딩 값을 이용해 예측

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2010.png)

1. 모든 node 임베딩 값을 평균내서 이용
2. 모든 node 임베딩 값들 중 최대값만 이용
3. 모든 node 임베딩 값들의 합을 이용
- 그러나 위 3가지 방법은 모두 **small graph에만** **적당**

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2011.png)

- 위 예시를 보면 전혀 다른 그래프인데도 같은 그래프처럼 나타내질 수 있음

그래서 나온것이.. → `Hierarchical Global Pooling` 위계 전역 풀링

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2012.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2013.png)

### Supervised vs Unsupervised Learning

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2014.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2015.png)

### Supervised

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2016.png)

- node : 네트워크, 어떤 분야에 속해있는지
- edge : 거래 간에 사기치는 것인지
- graph : 분자간의 어떤 건지, 약물 관련 그래프 등

### Unsupervised

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2017.png)

- node : clustering 계수, PageRank(추천 시스템 등)
- edge : 노드 사이에 숨겨진 edge 가 있는지
- graph : 그래프가 동형인지

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2018.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2019.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2020.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2021.png)

- Cross Entropy 는 Loss 라고 생각하면 됨.
→ Classification 문제에서 softmax 이후 생성된(모든 값 합이 1) 예측 값과 실제 값 사이에서 loss 를 구하는 방법
→ 여기서 실제 1인 곳의 loss만을 더해 최종 loss로 이용

[[PyTorch] 자주쓰는 Loss Function (Cross-Entropy, MSE) 정리](https://nuguziii.github.io/dev/dev-002/)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2022.png)

- Mean squared Error (MSE)
→ 회귀 문제에서 가장 인기있는 loss function

### Evaluation

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2023.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2024.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2025.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2026.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2027.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2028.png)

![Untitled](2%20Training%20Graph%20Neural%20Networks%20d540a0a3edbf495c8fd4ce1425a875ea/Untitled%2029.png)
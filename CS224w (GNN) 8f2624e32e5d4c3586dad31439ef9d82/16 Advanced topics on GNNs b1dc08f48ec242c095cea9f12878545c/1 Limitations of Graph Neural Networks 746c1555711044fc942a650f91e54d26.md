# 1. Limitations of Graph Neural Networks

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled.png)

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%201.png)

### 완벽한 GNN 이란?

→ 이웃 구조에 따라 다른 임베딩을 가지는 것

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%202.png)

- 두 노드가 같은 neighborhood structure를 가지면 같은 임베딩을 가지고,
- 다른 neighborhood structure를 가지면 다른 임베딩을 가지는 것

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%203.png)

- 그러나 observation 1과 2가 항상 옳은 것은 아님
    
    1의 경우(같은 구조인 경우)는 먼저
    
    → 서로 다른 노드가 나타났을 때 서로 다른 임베딩을 할 수 가 없음.
    
    → 이것을 해결하기 위해 **Position-aware GNN** 이용
    
    - 노드가 가지는 위치를 고려한 노드임베딩

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%204.png)

- 2번의 경우(구조가 다른 경우 다른 임베딩)는 
→ 특정 경우에 computational graph가 동일함
    
    → 이를 해결하기 위해 **Identity-aware GNN** 이용 ****
    
    - WL GNN 보다 효과적인 message passing GNN 모델

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%205.png)

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%206.png)

- 여기서 **실패한 모델**은 **항상 같은 임베딩을 나타내**는 것
- **성공한 모델**은 **다른 임베딩**을 나타내는 것

→ 즉 **임베딩은 GNN computation graph로 부터 결정**됨

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%207.png)

- 가장 단순한 방법으로는 One-hot encoding이 있음.

![Untitled](1%20Limitations%20of%20Graph%20Neural%20Networks%20746c1555711044fc942a650f91e54d26/Untitled%208.png)

- 스케일러블하지 않고,
- 귀납적이라는 이슈가 있음
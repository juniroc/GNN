# 17. Scaling Up GNN’s

- 방대한 크기의 그래프를 GNN을 통해 학습을 할 경우 Computation Cost 가 상당함
→ 이를 해결하기 위해 3가지 방법이 존재
    
    ### Neighbor Sampling
    
    - Neighbor Sampling 의 경우 GraphSAGE 방법대로 k-hops Neighbors 만으로 node embedding을 하는 것인데, 이는 똑같이 코스트가 많이 들기 때문에 일부만 Random walk 등으로 추려서 학습함 (아래 그림 참고)
    
    ![Untitled](17%20Scaling%20Up%20GNN%E2%80%99s%20cb95a97491e8461eb612d7ab4a0af1ba/Untitled.png)
    
    ---
    
    ### Cluster-GCN
    
    - 그래프 클러스터링을 통해 subgraph로 나눈 후 학습 (preprocessing : get subgraph → mini-batch training : subgraph를 이용한 학습) 
    → 이는 다른 그룹간에는 서로 message passing이 안되기 때문에 Advanced Cluster-GCN 이 나오는 배경이 됨
    → Advanced Cluster-GCN : 기존 Cluster-GCN에서 서로 다른 그룹간에 aggregation이 일어남
    
    ---
    
    ### Simplified-GCN
    
    - 기존 Vanilla GCN 에서는 k+1 layer를 k layer 의 neighborhood embedding layer 와 weight, activation function 을 통해 구했다면
    → simplified-GCN은 미리 k-hops neighborhood embedding 과 node feature 를 고정으로 미리 계산한 후 Weight들을 곱하는 방식으로 학습
    → 즉 pre-computed node feature에 영향을 받아 embedding
    

[1. Scaling Up Graph Neural Networks to Large Graphs](17%20Scaling%20Up%20GNN%E2%80%99s%20cb95a97491e8461eb612d7ab4a0af1ba/1%20Scaling%20Up%20Graph%20Neural%20Networks%20to%20Large%20Graphs%202701e69e454a4769a441409c88058a01.md)
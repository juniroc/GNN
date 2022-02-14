# 2. Position-aware GNN

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled.png)

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%201.png)

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%202.png)

- Structure-aware
→ **노드가 구조적인 역할에 의해 라벨링**
- **가끔** structure-aware일 경우 **GNN은 제대로 적용**되기도 함

그러나..

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%203.png)

- Position-aware
→ **노드의 위치**에 따라서 라벨링
- Position-aware 태스크에서는 **항상 실패 함(또는 실패하는 경우가 많음)**
    
    → ex) 위치적으로 대칭일 경우
    

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%204.png)

- key point 는 **Anchor**
    - Anchor 를 지정하면 그곳으로부터 얼마나 멀리 떨어져 있는지 계산

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%205.png)

- 실제로 여러개의 Anchor를 사용하여 좀 더 구체적으로 표현 가능
→ 단, 너무 많을 경우 계산복잡도 상승
- v_1 : (1, 2)
v_2 : (2, 1)

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%206.png)

- Anchor 세트라는 것을 지정할 수 있음(노드 세트)
→ S_1과 v_3 를 하나의 Anchor set 으로 설정
→ Anchor set 중 가장 가까운 노드와의 거리로 설정
→ 이때 v_3는 그 안에 포함되므로 거리가 0 이다.
- 큰 Anchor set 은 때로 정밀한 위치 계산을 제공
→ 이는 총 Anchor 갯수를 절약할 수 있음
- v_1 : (1, 2, 1)
v_2 : (1, 2, 0)

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%207.png)

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%208.png)

 

![Untitled](2%20Position-aware%20GNN%20e0f6b05994bc4305a65102c82699df02/Untitled%209.png)

- **Position-aware GNN 의 포인트
→ Anchor 개념을 이용해 인코딩한 것**
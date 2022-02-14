# 1. Graph Augmentation for GNNs

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%201.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%202.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%203.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%204.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%205.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%206.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%207.png)

- `cyclical` 한 그래프를 구별 못함

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%208.png)

- 즉 모든 경우에 동일하게 보일 것.
- 그러므로 feature augmentation이 필요함

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%209.png)

- 0부터 각각 n번째 cycle length를 가지는 위치에 인코딩

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2010.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2011.png)

- 노드의 feature를 강화하는 법
→ 가상의 엣지를 추가 → 두개의 홉 거리 이웃을 연결
→ A + A^2 를 이용 (이때 A 는 Adjacent Matrix)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2012.png)

- 가상의 노드 추가 → 멀리 떨어져있는 노드끼리 메시지 전달이 잘 일어나는 것으로 볼 수 있음.

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2013.png)

- 일부 (임의) 노드만 이웃노드에 메시지 전달하게 하는 방법

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2014.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2015.png)

![Untitled](1%20Graph%20Augmentation%20for%20GNNs%20001d8e74689e4cb2be32ade76c03d1ce/Untitled%2016.png)
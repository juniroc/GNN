# 3. Setting up GNN Prediction Tasks

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%201.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%202.png)

- train / validation / test set 분리
→ 그냥 random 이 제일 많이 쓰임

- 하지만 GNN에서는 스플릿을 함부로하면 안됨
→ 왜냐?

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%203.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%204.png)

- 위 ppt와 같이 만약 GNN에서 스플릿을 실행한다면 1과 5는 서로 메시지 패싱이 필요한데,
그러지 못하는 상황이 되어버림.

- 그러면 어떻게해야하나?

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%205.png)

- 그래프 전체를 그대로 묶어서 인풋으로 넣고 라벨만 나누어서 진행
    - `1, 2` 라벨은 학습 데이터로 이용
    - `3, 4` 라벨은 검증 데이터로 이용
    - `5, 6` 라벨은 테스트 데이터로 이용

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%206.png)

- 나눠진 노드끼리 묶고, 나머지 edges 끊어버림
    - 1, 2 노드만 해당된 그래프, 학습 데이터로 이용
    - 3, 4 노드만 해당된 그래프, 검증 데이터로 이용
    - 5, 6 노드만 해당된 그래프, 테스트 데이터로 이용
- 즉 독립된 그래프로 생각하고 학습, 검증, 테스트 진행

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%207.png)

- Transductive setting 은 하나의 그래프에서 노드를 나누어 학습/검증/테스트 한 것
- Inductive setting 은 하나의 그래프를 여러개로 나누어 학습/검증/테스트 한 것

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%208.png)

- Node Classification 에서는 두가지 방법 모두 쓰임

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%209.png)

- Graph Classification 에서는 Inductive setting 이 많이 쓰임
→ 기존에 없던 그래프를 테스트 해야하므로

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2010.png)

- Link Prediction 은 비지도 학습이 대부분
→ 직접 레이블을 생성하거나 데이터셋 분리를 진행해야함

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2011.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2012.png)

- Inductive link prediction split 의 경우
각 학습/검증/테스트 데이터셋 마다 `Message edge` 와 `Supervision edge(예측용 edge)` 가 포함됨

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2013.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2014.png)

- 학습할 경우 : `Message edges` 만을 이용해 학습
- 검증할 경우 : `Message edges` 와 `Supervision edges` 를 이용해 `Validation edges` 예측 하는 방법으로 검증
- 테스트할 경우 : `Message edges` , `Supervision edges` , `validation edges` 를 이용해 `test edges` 예측하는 방법으로 검증

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2015.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2016.png)

![Untitled](3%20Setting%20up%20GNN%20Prediction%20Tasks%20265e9d4f2f334ae4852f4fb5de43c63e/Untitled%2017.png)
# Link-level predict

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled.png)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%201.png)

- 랜덤으로 일부를 제거하고 그것을 예측하게끔 함
- t0 ~ t0' 기간동안 내용을 학습해 t1~t1' 를 예측함
- n 은 새로 생긴 엣지들

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%202.png)

# Link 설명을 위한 특징화 및 생성 방법3가지

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%203.png)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%204.png)

- 여기에 나아가서 B와 H는 2개의 공통 이웃 노드를 공유하지만, A와 E는 1개만 공유함
→ 이것을 이용해서 연결을 특징화 할 수 있음

### Local Neighborhood overlap

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%205.png)

- Jaccard's Coefficient = (실제 공유 이웃) / (A와 B가 각각 공유하는 전체 이웃)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%206.png)

- local-neighborhood overlap 의 한계점은 **서로 공유 이웃하는 노드가 없을 경우 항상 0
→ 또는 2홉 이상 떨어져 있는 경우도 항상 0**

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%207.png)

- 노드의 사이의 거리를 계산 방법 : 근접 메트릭스 이용

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%208.png)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%209.png)

- A^(N) = N 번째에 도달할 수 있는 횟수
- ex) (3,4) 는 2번의 엣지를 지나서 도달할 수 있는 방법이 없어서 0

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%2010.png)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%2011.png)

![Untitled](Link-level%20predict%209ca7eebd7e8c47daad739ca0bb0c2035/Untitled%2012.png)
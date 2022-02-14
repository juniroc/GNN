# 2. Designing the Most Powerful Graph Neural Network

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%201.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%202.png)

- same color proportion의 multi-set 구별 불가능

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%203.png)

- mean-poolling 과 max-pooling의 차이를 알아보자

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%204.png)

- mean-pooling 은 위 두가지를 구분 못함

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%205.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%206.png)

- 위 2개의 캡쳐만 봐도 왜 그런지 이해할 수 있음

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%207.png)

- max-pooling(GraphSAGE) 또한 어떤 경우는 구별 불가능

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%208.png)

- 위 세가지 경우 모두 같은 인코딩을 갖을 수 있음
→ 즉 구별이 불가능

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%209.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2010.png)

- 이것들을 효과적으로 풀어주는 design이 있음
**→ Model Injective multiset function**

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2011.png)

- 각 함수를 모두 더함

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2012.png)

- 즉 각 노드별로 함수를 통해 나온 값을 더하는 방법

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2013.png)

- 그럼 어떤 종류의 함수를 이용할 것인가?
→ MLP
- 왜 MLP 인가?
→ 성능이 좋아서.. 원하는 히든 차원을 생성할 수 있음
→ 주로 100 ~ 500 사이가 적당함

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2014.png)

- 주로 히든레이어는 100~500차원이 적당함
→ 주입성 보존을 위해

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2015.png)

- GIN - Graph Isomorphism Network
- 메시지 전달이 가장 뛰어난 그래프 신경망

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2016.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2017.png)

- u 는 k번째에서의 이웃 노드

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2018.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2019.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2020.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2021.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2022.png)

- 엡시론은 학습 가능한 변수

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2023.png)

- MLP레이어에서 오른쪽(u)은 이웃에 대한 정보이며 왼쪽(v)은 합계에 대한 의미
→ 즉 다음 단계로 넘어갈 때 메시지가 사라지지 않음

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2024.png)

- 해쉬대신 GINConv를 이용한

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2025.png)

- GIN 의 장점 (WL Graph kernel 보다 나은) - 노드 차이를 잘 포착할 수 있음

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2026.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2027.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2028.png)

![Untitled](2%20Designing%20the%20Most%20Powerful%20Graph%20Neural%20Network%20f8da4f41cf114d7191ca78c317132963/Untitled%2029.png)
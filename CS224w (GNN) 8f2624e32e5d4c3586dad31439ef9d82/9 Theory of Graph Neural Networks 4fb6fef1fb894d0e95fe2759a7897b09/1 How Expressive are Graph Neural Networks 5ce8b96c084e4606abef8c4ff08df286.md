# 1. How Expressive are Graph Neural Networks

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%201.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%202.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%203.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%204.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%205.png)

- GCN : (mean - pool)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%206.png)

- GraphSage : (max-pool)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%207.png)

- feature 가 모두 같을 경우 위 그래프와 같이 표현(같은 색상)이 되지만
- 어떻게 다른 구조인 경우 나타낼 수 있을까?

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%208.png)

- 1과 5는 각각 다른 수의 degrees 이므로 구분하기 쉬운

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%209.png)

- 1, 4 는 여전히 같은 차수 2이지만 이웃이 다름

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2010.png)

- 1, 2 는 서로 대칭관계임

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2011.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2012.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2013.png)

- 숫자(feature)가 있는 경우는 서로 다른 구조로 보임

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2014.png)

- 숫자가 없는 경우 1, 2 는 같은 구조로 보임

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2015.png)

- 즉 결구 GNN은 1, 2 모두 같은 임베딩을 생성함

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2016.png)

- 역시 1과 2 는 구분이 안됨 feature가 동일할 경우

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2017.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2018.png)

- 1, 2 는 같은 구조이므로 같은 임베딩(같은 색), 나머지는 각각의 임베딩을 갖음

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2019.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2020.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2021.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2022.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2023.png)

![Untitled](1%20How%20Expressive%20are%20Graph%20Neural%20Networks%205ce8b96c084e4606abef8c4ff08df286/Untitled%2024.png)
# 1. Introduction : Structure of Graphs

### 그래프 데이터의 종류

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%201.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%202.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%203.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%204.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%205.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%206.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%207.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%208.png)

### GNN 이 어려운 점

- 기준점이 없음.

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%209.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2010.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2011.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2012.png)

 

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2013.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2014.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2015.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2016.png)

# Node-Level

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2017.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2018.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2019.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2020.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2021.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2022.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2023.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2024.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2025.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2026.png)

- 약물 종류가 워낙 많아서(당연히 조합도 다양해서) 부작용이 발생하는지 실험적으로 또는 임상 시험에서 테스트할 수는 없음.
    
    → 이를 GNN 으로 한 쌍의 약물에 대해 이러한 약물이 상호 작용하는 방식과 어떤 종류의 부작용이 발생할 수 있는지 예측하는 예측 엔진을 구축할 수 있는가?
    
    ![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2027.png)
    
- 2단계 이질적 네트워크
    
    **삼각형 → 다른 약물**
    
    **원 → 몸의 단백질**
    

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2028.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2029.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2030.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2031.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2032.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2033.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2034.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2035.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2036.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2037.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2038.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2039.png)

 

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2040.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2041.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2042.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2043.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2044.png)

- **2E 인 이유 → 가장자리가 2개여서 2번 계산되므로**

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2045.png)

### 이분 그래프

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2046.png)

- Bipartite Graph (이분 그래프)

→ 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2047.png)

- 보통 논문 관련해서 왼쪽은 저자 오른쪽은 논문 이런식으로 작성하는 경우도 있음
- 공동 저자 등 참고 논문 등

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2048.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2049.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2050.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2051.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2052.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2053.png)

노드와 엣지는 각각 성질을 가질 수 있음.

ex) 노드 : 남/녀, 나이
      엣지 : 관계, 결합 종류

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2054.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2055.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2056.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2057.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2058.png)

- F → G 로 가는 엣지가 없어서 이것은 **약한 결합**임

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2059.png)

![Untitled](1%20Introduction%20Structure%20of%20Graphs%20353e82fb2d674a7390a51f9772d359c6/Untitled%2060.png)
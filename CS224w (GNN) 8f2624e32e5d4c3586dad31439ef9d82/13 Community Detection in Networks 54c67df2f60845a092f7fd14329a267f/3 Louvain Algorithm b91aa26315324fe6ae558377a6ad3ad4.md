# 3. Louvain Algorithm

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled.png)

- 커뮤니티를 찾아내는 알고리즘

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%201.png)

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%202.png)

- Phase 1 : Modularity 최적화
    
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%203.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%204.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%205.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%206.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%207.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%208.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%209.png)
    
    ![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2010.png)
    

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2011.png)

- 위 계산 과정을 했을 때 결과값 (Q_delta) 가 0 보다 클 경우 업데이트를 해줌

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2012.png)

- 위 과정을 반복하고 변화가 없을 때

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2013.png)

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2014.png)

- step 2 Graph
    - 개인 회귀 edge는 내부 edge 갯수 * 2
    - 외부 edge 는 외부로 연결된 edge

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2015.png)

![Untitled](3%20Louvain%20Algorithm%20b91aa26315324fe6ae558377a6ad3ad4/Untitled%2016.png)

- Modularity 가 증가하는 방향으로 진행되며
- 최적의 경우를 찾아내는게 목적

- Phase 2 : 식별된 커뮤니티 집계
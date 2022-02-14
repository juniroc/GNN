# 3. Identity-Aware GNN

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled.png)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%201.png)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%202.png)

- Node-level 에서도 그래프가 구분이 안됨 (Node가 다른 경우)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%203.png)

- Edge-level 에서도 구분이 안됨 (edge가 다른 경우)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%204.png)

- Graph-level 또한 구분 안됨

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%205.png)

- 해결법
→ 노드에 컬러를 부여하는 것

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%206.png)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%207.png)

- node-level 에서 Different Computation graph 이슈 해결 가능

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%208.png)

- graph-level 에서도 해결 가능

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%209.png)

- Edge-level 에서도 해결 가능

### 어떻게 node coloring 을 이용할 수 있나?

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2010.png)

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2011.png)

- 일반적인 GNN 에서 NN 모델을 한개만 이용했다면

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2012.png)

- ID-GNN에서는 서로 다른 NN모델 2개 이상을 적용
→ 서로 다른 메시지 전달

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2013.png)

- v_1 과 v_2가 같은 computational graph 구조를 가졌지만, 다른 node colorings를 가짐
→ 이는 다른 NN 을 이용해 embedding computation을 적용
→ embedding 결과가 다름

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2014.png)

- ID-GNN은 node 의 cycles를 카운트 가능함.
→ GNN보다 더 좋은 성능을 가짐

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2015.png)

- Cycle count

![Untitled](3%20Identity-Aware%20GNN%20951cc13f48c049eebc41450c39f945a5/Untitled%2016.png)

- **ID-GNN은 any message passing GNN(GCN, GraphSAGE, GIN, ...) 등으로 적용 가능함**
- ID-GNN이 기존 GNN 보다 효과적이며, 1-WL 보다 효과적임
- **ID-GNN을 쉽게 적용하기 위한 PyG, GDL, ... 등 다양한 툴이 있음**
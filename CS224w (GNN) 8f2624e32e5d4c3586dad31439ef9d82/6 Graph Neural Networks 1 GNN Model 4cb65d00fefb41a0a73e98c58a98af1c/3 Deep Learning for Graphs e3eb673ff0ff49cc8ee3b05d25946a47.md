# 3. Deep Learning for Graphs

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%201.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%202.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%203.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%204.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%205.png)

- cnn으로 학습하기엔 그래프의 locality와 sliding 을 정의하기 애매한 문제

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%206.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%207.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%208.png)

![Untitled](../220128%20Review%20(GCN)%204c025ddb611741a08eaa348a94578105/Untitled%201.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%209.png)

- 여기서 E, F 는 구조가 같음을 확인할 수 있음

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2010.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2011.png)

- 오른쪽의 Ⓑ노드를 보면 (A, C)와 연결되어있는데, 이는 (C, A) 순서가 바뀌어도 같은 값을 나타내야함
→ **키 구별은 얼마나 다른 집합으로부터 접근이 되었는지로 구분**

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2012.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2013.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2014.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2015.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2016.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2017.png)

 

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2018.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2019.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2020.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2021.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2022.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2023.png)

![Untitled](../220128%20Review%20(GCN)%204c025ddb611741a08eaa348a94578105/Untitled%202.png)

![Untitled](../220128%20Review%20(GCN)%204c025ddb611741a08eaa348a94578105/Untitled%203.png)

![Untitled](../220128%20Review%20(GCN)%204c025ddb611741a08eaa348a94578105/Untitled%204.png)

![Untitled](../220128%20Review%20(GCN)%204c025ddb611741a08eaa348a94578105/Untitled%205.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2024.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2025.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2026.png)

![Untitled](3%20Deep%20Learning%20for%20Graphs%20e3eb673ff0ff49cc8ee3b05d25946a47/Untitled%2027.png)

- GNN 은 이웃 정보를 집계하여 노드에 대한 embedding
→ 학습 진행 후에 추가 임베딩 가능
→ 속성 정보(parameter) 저장이 가능해 추가 이용 가능
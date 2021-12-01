# PicTory : 이미지를 통한 맞춤형 여행지 추천         
     
### Web Part
> frontend : HTML, Javascript, css   
  backend : Django, MySQL
        
### 💛 프로젝트 개요
이름 입력 후 3번의 이미지 선택을 통해 맞춤형 여행지를 추천받을 수 있는 웹 페이지
     - 사용자는 3회 이상의 피드백 요청부터 응답률이 급격히 떨어지는 경향을 보임 
     - 이미지 선택 시 암시적 데이터를 통해 필요한 정보를 추출하고 취향에 맞는 여행지를 추천하려 함    

### 💚 웹 구성
     - 접근성이 좋은 휴대폰으로도 사용가능하도록 반응형 웹으로 구현
     
- **초기 진입 화면 (index.html)**   
     - 사용자는 이름 입력 후, 이미지 선택 화면(main.html)으로 진입 가능   
     - 서비스에 대한 소개가 표시   
     - 사용자 위치 정보 수집이 허용되면 사용자 근처 관광지에 대한 정보가 표시, 거부되면 랜덤으로 표시          
     - 관광지는 모달창을 통해 자세히 볼 수 있으며, 카카오 지도 api를 통해 위치 알 수 있음        
     
     <img src="https://user-images.githubusercontent.com/80735829/144225141-184edd3c-fcce-43f4-88c7-c7832294f2e9.png"  width="420" height="250"/> <img src="https://user-images.githubusercontent.com/80735829/144225236-f3351f26-0b89-4a5f-9c65-8a8b549346ac.png"  width="420" height="250"/>    
      <img src="https://user-images.githubusercontent.com/80735829/144225969-1343b78e-1458-485c-a52a-8e961ae28b0f.png"  width="420" height="250"/> <img src="https://user-images.githubusercontent.com/80735829/144226042-814c24d1-2c7b-42eb-8671-85bf1fb493fc.png"  width="420" height="250"/> 
      
         
- **이미지 선택 화면 (main.html)**    
     - 사용자는 이름 입력 후에 이미지를 선택해야함 
     - 6장의 사진이 3번 주어짐    
     - 1번째 제시 사진은 클러스터 중 6개를 무작위로 선정하여 각 클러스터 내 랜덤 이미지를 제시
     - 2, 3번째 제시 사진은 이전에 선택한 사진 내에 있는 클러스터 사진 위주로 제시    
     
     <img src="https://user-images.githubusercontent.com/80735829/144226687-a81d8bc1-228d-4555-a451-64cfdba2f1f3.png"  width="420" height="250"/>


- **추천 결과 화면 (result.html)**    
     - 이미지 선택 3회를 완료 시 마지막 사진을 기반으로 한 최종 결과인 관광지 이미지 3장이 출력됨
     - 각 관광지를 선택 시 모달창으로 세부 정보를 확인 가능     
     - 사용자는 추천 받은 결과에 대해 만족도 평가 가능     

     <img src="https://user-images.githubusercontent.com/80735829/144227030-f41e465f-991a-461b-ab24-222f4f3e2044.png"  width="420" height="250"/>   <img src="https://user-images.githubusercontent.com/80735829/144227112-a3f4d267-f208-430f-8a93-cb21989aea89.png"  width="420" height="250"/>   
     
     



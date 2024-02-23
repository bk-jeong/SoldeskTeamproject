function test(testalldata) {
    //var testalldata=document.getElementById("alldata");
    
    // alert(testalldata)
    // alert(typeof(testalldata))
    // alert(testalldata['01_bigi'])
    
    var datakeys=Object.keys(testalldata);
    
    //각 각인별 데이터 분리하기
    var testdatas=Object.values(testalldata);
    
    var zero=new Array(datakeys.length)
    // 빈 변수값 
    var testdata='';
    // 그래프 에 들어갈 정보들을 한번에 모아두기
    var pieChartData=new Array(datakeys.length);
    for (let i = 0; i < testdatas.length; i++) {  //각인 수만큼 작업하게 하기
        testdata=testdatas[i];
        var testkey=Object.keys(testdata);  //키값 가져오기
        var testvalue=Object.values(testdata); // 벨류값 가져오기
        
        
        zero[i]=testvalue;
        for (let index = 0; index < testkey.length; index++) {  //키값에 벨류값을 퍼센트로 계산하여 넣어주는 작업
            testkey[index]= testkey[index]+"("+(testvalue[index]*100)+"%)"
        }
        
        pieChartData[i]={   // 그래프에 들어갈 데이터를 정리하는 작업
          labels:testkey,  // 그래프 분류기준인 이름값이 들어가는곳
          datasets: [{  // 분류된 데이터 
            data:testvalue,  // 데이터 값
            backgroundColor:['red','blue','pink','black','gray','skyblue'], // 데이터별 색상 선택
          }]
        };
      };
    //let pieChartDraw=function(){  // 데이터를 그래프로 만드는 작업
      for (let i = 0; i < datakeys.length; i++) {
          let ctx= document.getElementById(datakeys[i]).getContext('2d');  // 2D형 데이터를 만든다 선언
          window.pieChert= new Chart(ctx,{   //만들 그래프의 옵션 설정
            type:'pie',   // 그래프 타입은 원형 (파이구조)
            data:pieChartData[i],  // 만들어둔 데이터 등록
            options: {   // 여러 옵션 설정
                responsive:false,  // 윈도우 사이즈변동에 따른 그래프 그기 변동 막아주는 기능
                plugins:{  // 그래프 내부 옵션 변경을 위한 세부 설정
                    legend: { // 나눈 티어 이름들을 보여주는 옵션
                        position: 'top', // 우측으로 이동
                        align:'start', // 상단으로 이동
                        maxWidth : 300,
                        labels:{
                            boxWidth: 15,
                            usePointStyle: true,
                            pointStyle: 'circle',
                            color : '#124521',
                            filter: function(legendItem) {
                                return zero[i][legendItem.index] != 0 
                            }
                          }
                        },
                    tooltip: {  // 마우스 올리면 보이는 툴팁 설정
                        enabled:false // 툴팁 해제
                    },
                  }
              }
          });
          document.getElementsByClassName("tooltip_image")[i].style.display = 'none';
      //}
        };
    }


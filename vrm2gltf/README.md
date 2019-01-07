# vrm2gltf
VRoid에서 .vrm으로 Export된 파일을 gltf로 바꿉니다.

## 하는 일
vrm 파일을 gltf로 변환하고 VRM 확장을 제거합니다.

## 실행법
```
vrm2gltf.bat <source .vrm file> <target .gltf file without extension>
```

## 예제
```
vrm2gltf.bat Sendagaya_Shibu.vrm test
```

## 결과물
- \<target .gltf file without extension>.gltf

## 요구사항
- Windows10
- VRoid 0.5.1 대응
- python 3.5+
- [gltf-pipeline](https://github.com/AnalyticalGraphicsInc/gltf-pipeline)

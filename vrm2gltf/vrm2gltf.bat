@echo off

copy %1 %2.glb

call gltf-pipeline -i %2.glb -o %2.gltf

del %2.glb

call python vrm-extensison-remover.py %2.gltf

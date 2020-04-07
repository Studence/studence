cd protos
echo [COMPILEING  UIPROTOS AND PROTOS]
protoc summaryUiPb.proto --python_out=..\Protobuff
protoc nameUiPb.proto --python_out=..\Protobuff
protoc namePb.proto --python_out=..\Protobuff
protoc timeUiPb.proto --python_out=..\Protobuff
protoc timePb.proto --python_out=..\Protobuff
protoc entityUiPb.proto --python_out=..\Protobuff
protoc entityPb.proto --python_out=..\Protobuff
protoc organisationUiPb.proto --python_out=..\Protobuff
protoc organisationPb.proto --python_out=..\Protobuff
cd ..

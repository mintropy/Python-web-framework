# Django + DRF with pydantic
- DRF에서 serializer대신 pydantic으로 진행하는 프로젝트입니다.
    - pydantic은 data validation을 위한 python library입니다.

# 특징
- pydantic의 BaseModel을 Django model 기반으로 하여 작성 및 validation 진행
    - [공식문서](https://pydantic-docs.helpmanual.io/benchmarks/)에 따르면 DRF serializer가 pydantic validation보다 12배 이상 느리다 함

# 장점

# 단점
- DRF serializer의 편의기능을 모두 구현해줘야함
    - Django model object, queryset을 편리하게 응답 데이터까지 변환해주는 과정에서 추가적인 작업이 많이 필요함
    - data validation은 잘 동작하지만, serializer의 .is_valid(), .data(), .errors()와 같은 편리기능을 수동적으로 구현해야함
        - .errors()는 실서비스에서는 사용하지 않더라도 개발과정에서 어떤 validation이 실패했는지 보여주는 편리한 기능인데, 해당 부분도 수동적으로 확인해야하는 번거로움이 있음

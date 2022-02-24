# 같은 기능을 서로 다른 Python Web Framework로 구현하는 프로젝트입니다.
- 같은 DB, API를 바탕으로 제작되었습니다

1. Django + DRF(serializer)
2. Django + DRF(pydantic)
3. Django + django-ninja
4. FasAPI

---
# ERD
```mermaid
erDiagram
User {
    int id
    str username
    str password
}
Article {
    int id
    str(20) title
    str content
    datetime created_at
    datetime updated_at
}
Reply {
    int id
    str(100) content
    datetime created_at
    datetime updated_at
}

User }o--|| Article : write
User }o--|| Reply : write
Article }o--|| Reply : contain
```

# API

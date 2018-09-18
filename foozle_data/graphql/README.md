``` query User {
  getUserById(id: "b2625c38-c587-4f01-813a-dd6eaceb165d") {
    id
    navigation {
      sessionId
      createdAt
      userInfo
    }
  }
}

query Project {
  getAllProjects {
    name
    navigationSet {
      sessionId
      pages {
        id
      }
      user {
        uniqueId
      }
    }
  }
}

query Navigation {
  getAllNavigations {
    id
    allPages(id: "2") {
      id
    }
  }
}
```
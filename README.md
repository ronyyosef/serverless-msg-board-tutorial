This is a msg board CURD application.

To deploy run "serverless deploy"

endpoints:
* GET - https://5l592v8bni.execute-api.us-west-2.amazonaws.com/dev/msg-board
* GET - https://5l592v8bni.execute-api.us-west-2.amazonaws.com/dev/msg-board/{pk}
* POST - https://5l592v8bni.execute-api.us-west-2.amazonaws.com/dev/msg-board
* PUT - https://5l592v8bni.execute-api.us-west-2.amazonaws.com/dev/msg-board/{pk}
* DELETE - https://5l592v8bni.execute-api.us-west-2.amazonaws.com/dev/msg-board/{pk}

functions:
* GetMsgBoardList: msg-board-dev-GetMsgBoardList (8.7 kB)
* GetMsgBoardItem: msg-board-dev-GetMsgBoardItem (8.7 kB)
* PostMsgBoard: msg-board-dev-PostMsgBoard (8.7 kB)
* UpdateMsgBoard: msg-board-dev-UpdateMsgBoard (8.7 kB)
* DeleteMsgBoard: msg-board-dev-DeleteMsgBoard (8.7 kB)

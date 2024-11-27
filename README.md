# P2P-Remote-Shell
セキュリティ対策意識として、どこかの誰かのためのわかりやすい資料として作ろうと思ったら
案外サクッとできてしまったものです。

P2P経由でコマンドを加害者側が送信し、被害者側が受け取ったコマンドを実行、その後その結果を加害者側に送信するPythonプログラムです。
ただしプログラムの都合上、コマンドを実行しきった後でないと実行結果が出力されません。SSHの代理にはならないのでご了承を。(なおそのままでは動かないようにしています。)

P2P/Socket通信での接続のため、正直常用使いでも危険です。
あくまでも「このコード数で作れるんだ。」といった学習用/危険感受性向上目的としてお使いください。
またどうしても実行する際は信頼できるローカルLAN内や、VPNを介して行ってください。

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

### Permissions
- **Commercial use**: You can use this project for commercial purposes.
- **Modification**: You can modify the code as you wish.
- **Distribution**: You can share this project freely.
- **Private use**: You can use this project in private.

### Limitations
- **Liability**: The author is not responsible for any damages caused by using this project.
- **Warranty**: This project is provided "as-is," without any warranty of any kind.

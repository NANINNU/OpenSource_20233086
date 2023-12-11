import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLabel, QVBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from googleapiclient.discovery import build

def resourcePath(relativePath):
    basePath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(basePath, relativePath)

formClass = uic.loadUiType("projectMainui.ui")[0]

class HyperlinkListWidgetItem(QListWidgetItem):
    def __init__(self, text, url, list_widget):
        super(HyperlinkListWidgetItem, self).__init__()

        label = QLabel(f'<a href="{url}">{text}</a>')
        label.setOpenExternalLinks(True)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setSizeHint(label.sizeHint())

        # list_widget에 아이템을 추가하는 것이 올바릅니다.
        list_widget.addItem(self)

class Worker(QRunnable):
    def __init__(self, query, list_widget):
        super(Worker, self).__init__()
        self.query = query
        self.list_widget = list_widget

    @pyqtSlot()
    def run(self):
        api_key = "AIzaSyDnzxPcAiNwgNffR0gYTypexRzPOgiR0qE"
        cse_id = "f4f53faad40704d43"
        service = build("customsearch", "v1", developerKey=api_key)

        links = []
        titles = []
        contents = []

        res = service.cse().list(q=self.query, cx=cse_id).execute()
        for item in res.get("items", [])[:3]:
            links.append(item['link'])
            titles.append(item['title'])
            contents.append(item.get('snippet', 'N/A'))

        num_results = len(links)

        print(f"Number of results: {num_results}")

        for i in range(num_results):
            link_item = HyperlinkListWidgetItem("링크", links[i], self.list_widget)
            title_item = QListWidgetItem(titles[i])
            content_item = QListWidgetItem(contents[i])

            self.list_widget.addItem(title_item)
            self.list_widget.addItem(content_item)

            print("제목:", titles[i])
            print("본문:", contents[i])

class WindowClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listwidget = QListWidget()  # QListWidget을 정의해야 합니다.
        self.listwidget.itemClicked.connect(self.open_link)  # itemClicked 시그널에 슬롯 연결
        self.searchButton.clicked.connect(self.windowList)
        
        self.verticalLayout.addWidget(self.listwidget)

    def windowList(self):
        userInput = self.ErrorMessage.text()
        search_query = [userInput + " : tistory.com",
                        userInput + " : reddit.com",
                        userInput + " : stackoverflow.com",
                        userInput + " : github.com"]

        for query in search_query:
            worker = Worker(query, self.listwidget)
            QThreadPool.globalInstance().start(worker)

    def open_link(self, item):
        # itemClicked 시그널에 의해 호출되는 슬롯
        # 아이템이 하이퍼링크인 경우 브라우저에서 해당 링크 열기
        if isinstance(item, HyperlinkListWidgetItem):
            url = item.text()
            QDesktopServices.openUrl(QUrl(url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())

const { app, BrowserWindow } = require('electron/main')
const { autoUpdater } = require("electron-updater");

const createWindow = () => {
  const win = new BrowserWindow({
    
  });
  win.maximize();

  win.loadFile('index.html')
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
});
    autoUpdater.checkForUpdatesAndNotify();


autoUpdater.on("update-available", () => {
    console.log("Update available!");
});

autoUpdater.on("update-downloaded", () => {
    console.log("Update downloaded. It will be installed on restart.");
});


app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
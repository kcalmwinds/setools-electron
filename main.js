const { app, BrowserWindow } = require('electron/main')
//const { updateElectronApp } = require('update-electron-app');



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

//updateElectronApp(); // additional configuration options available

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
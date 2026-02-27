const { chromium, devices } = require('playwright');

const url = process.argv[2] || 'https://9301c365.cbse-migracao-v3.pages.dev';
const device = devices['iPhone 14'];

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ ...device });
  const page = await context.newPage();
  
  await page.goto(url, { waitUntil: 'networkidle' });
  
  // Measure title
  const metrics = await page.evaluate(() => {
    const title = document.querySelector('p.font-factul');
    if (!title) return { error: 'title not found' };
    return {
      titleWidth: title.getBoundingClientRect().width,
      bodyWidth: document.body.getBoundingClientRect().width,
      innerWidth: window.innerWidth,
      clientWidth: document.documentElement.clientWidth,
      scrollbarVisible: window.innerWidth !== document.documentElement.clientWidth,
      titleLines: Math.round(title.getBoundingClientRect().height / parseFloat(getComputedStyle(title).lineHeight))
    };
  });
  
  console.log('Device:', device.viewport.width + 'x' + device.viewport.height);
  console.log('Metrics:', JSON.stringify(metrics, null, 2));
  
  await page.screenshot({ path: 'data/screenshots/mobile-emulated.png', fullPage: true });
  console.log('Screenshot saved: data/screenshots/mobile-emulated.png');
  
  await browser.close();
})();

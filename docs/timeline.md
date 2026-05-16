<style>
  .tl-wrapper {
    --gold: #c9a95c;
    --steel: #4a90d9;
    --steel-bright: #64b5f6;
    --ice: #e8edf2;
    --ice-dim: #b0bec5;
    max-width: 860px;
    margin: 0 auto;
  }

  .tl-hero {
    padding: 32px 0 24px;
    border-bottom: 1px solid rgba(74,144,217,0.1);
    margin-bottom: 32px;
    animation: tlFadeUp 0.6s ease;
  }
  .tl-hero h1 {
    font-family: Georgia, 'Noto Serif SC', serif !important;
    font-size: 48px !important;
    font-weight: 400 !important;
    color: var(--ice) !important;
    line-height: 1.15 !important;
    letter-spacing: -0.03em !important;
    border: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .tl-hero-sub {
    font-size: 14px;
    color: var(--ice-dim);
    letter-spacing: 0.02em;
    margin-top: 4px;
  }

  .tl-month {
    margin-bottom: 28px;
    animation: tlFadeUp 0.6s ease both;
  }

  .tl-month h2 {
    font-family: Georgia, serif !important;
    font-weight: 400 !important;
    border: none !important;
    padding-left: 0 !important;
    font-size: 1.35em !important;
    color: var(--gold) !important;
    margin-bottom: 12px !important;
  }
  .tl-month h2::after {
    content: '';
    display: block;
    width: 40px; height: 2px;
    background: var(--gold);
    margin-top: 6px;
    opacity: 0.5;
  }

  .tl-day-group {
    margin-bottom: 20px;
  }
  .tl-day-group h3 {
    font-size: 0.95em !important;
    color: var(--steel-bright) !important;
    margin-bottom: 8px !important;
    font-weight: 500 !important;
  }

  .tl-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.89em;
  }
  .tl-table thead th {
    font-size: 0.75em;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #5c6e84;
    font-weight: 500;
    padding: 0 12px 8px;
    text-align: left;
  }
  .tl-table thead th:last-child { text-align: center; }
  .tl-table thead th:first-child { text-align: center; width: 50px; }

  .tl-table tbody td {
    padding: 7px 12px;
    color: var(--ice-dim);
    border-bottom: 1px solid rgba(74,144,217,0.05);
    transition: background 0.2s;
  }
  .tl-table tbody tr:hover td {
    background: rgba(74,144,217,0.04);
  }
  .tl-table tbody td:first-child {
    text-align: center;
    font-size: 0.78em;
    color: var(--gold);
    font-weight: 500;
    letter-spacing: 0.06em;
  }
  .tl-table tbody td:last-child { text-align: center; }
  .tl-table a {
    color: var(--steel) !important;
    border: none !important;
    text-decoration: none;
  }
  .tl-table a:hover { color: var(--steel-bright) !important; }

  .tl-stats {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 1px;
    background: rgba(74,144,217,0.06);
    border: 1px solid rgba(74,144,217,0.08);
    border-radius: 4px;
    overflow: hidden;
    margin: 32px 0 16px;
    animation: tlFadeUp 0.6s ease 0.3s both;
  }
  .tl-stat {
    background: rgba(13,31,53,0.5);
    padding: 20px 16px;
    text-align: center;
    transition: background 0.2s;
  }
  .tl-stat:hover { background: rgba(17,40,64,0.6); }
  .tl-stat-num {
    font-family: Georgia, serif;
    font-size: 30px;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 3px;
  }
  .tl-stat-label {
    font-size: 10px;
    color: var(--ice-dim);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  @keyframes tlFadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 768px) {
    .tl-hero h1 { font-size: 32px !important; }
    .tl-stats { grid-template-columns: repeat(2, 1fr); }
    .tl-table { font-size: 0.8em; }
  }
</style>

<div class="tl-wrapper">

<div class="tl-hero">
  <h1>更新时间线</h1>
  <div class="tl-hero-sub">按时间倒序展示所有研究报告的发布记录</div>
</div>

<div class="tl-month" style="animation-delay:0.08s">
<h2>2026年5月</h2>

<div class="tl-day-group">
<h3>5月17日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>策略</td><td>八维投资分析体系 — 方法论总纲（策略框架 #1）</td><td><a href="../research/eight-dimension-framework/">→</a></td></tr>
<tr><td>策略</td><td>仓位管理与风控六原则（策略框架 #2）</td><td><a href="../research/position-management-2026-05/">→</a></td></tr>
<tr><td>策略</td><td>渗透率 S 曲线择时体系（策略框架 #3）</td><td><a href="../research/s-curve-timing-system-2026-05/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月16日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>事件</td><td>特朗普访华（5.13-15）— 八维框架+行业深度影响</td><td><a href="../research/trump-china-visit-2026-05/">→</a></td></tr>
<tr><td>行业</td><td>美光访华与中芯扩产 — 双面棋局深度分析</td><td><a href="../research/micron-smic-china-expansion-2026-05/">→</a></td></tr>
<tr><td>宏观</td><td>W20 周度深度报告（5.11-16）</td><td><a href="../research/weekly-briefing-2026-05-16/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月11日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>事件</td><td>汉坦病毒邮轮疫情 — 安第斯毒株风险评估</td><td><a href="../research/hantavirus-cruise-outbreak-2026-05/">→</a></td></tr>
<tr><td>宏观</td><td>W19周度宏观快报（5.4-10）</td><td><a href="../research/weekly-briefing-2026-05-11/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月10日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>组合</td><td>华为哈勃5股组合 — 国产替代×硬科技</td><td><a href="../research/huawei-hubble-portfolio-2026-05/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月5日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>宏观</td><td>五一假期宏观深度复盘</td><td><a href="../research/macro-mayday-2026-05/">→</a></td></tr>
<tr><td>行业</td><td>CPU 涨价周期深度分析</td><td><a href="../research/cpu-price-cycle-analysis-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>澜起科技 (688008) 深度研究</td><td><a href="../research/montage-688008-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>阿里巴巴 (9988.HK) 深度研究</td><td><a href="../research/alibaba-baba-deep-dive-2026-05/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月4日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>行业</td><td>全球存储产业链</td><td><a href="../research/global-storage-industry-full-chain-analysis-2026-05/">→</a></td></tr>
<tr><td>行业</td><td>国产 GPU 全面对比</td><td><a href="../research/china-gpu-comprehensive-comparison-2026-05/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月3日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>事件</td><td>2026年巴菲特股东大会</td><td><a href="../research/buffett-brk-2026-shareholder-meeting/">→</a></td></tr>
</tbody>
</table>
</div>

<div class="tl-day-group">
<h3>5月1日</h3>
<table class="tl-table">
<thead><tr><th>类型</th><th>报告</th><th>链接</th></tr></thead>
<tbody>
<tr><td>个股</td><td>台积电 TSMC (TSM) 深度研究</td><td><a href="../research/tsmc-tsm-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>英伟达 NVIDIA (NVDA) 深度研究</td><td><a href="../research/nvidia-nvda-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>谷歌 Google (GOOGL) 深度研究</td><td><a href="../research/google-googl-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>闪迪 SanDisk (SNDK) 深度研究</td><td><a href="../research/sandisk-sndk-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>美光科技 Micron (MU) 深度研究</td><td><a href="../research/micron-mu-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>SK海力士 (000660) 深度研究</td><td><a href="../research/sk-hynix-000660-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>三星电子 (005930) 深度研究</td><td><a href="../research/samsung-005930-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>中际旭创 (300308) 深度研究</td><td><a href="../research/zhongji-innolight-300308-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>中芯国际 (0981.HK) 深度研究</td><td><a href="../research/smic-0981hk-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>华虹半导体 (1347.HK) 深度研究</td><td><a href="../research/huahong-1347hk-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>贵州茅台 (600519) 深度研究</td><td><a href="../research/moutai-600519-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>海光信息 (688041) 深度研究</td><td><a href="../research/hygon-688041-deep-dive-2026-05/">→</a></td></tr>
<tr><td>个股</td><td>摩尔线程 (688795) 深度研究</td><td><a href="../research/moore-threads-688795-deep-dive-2026-05/">→</a></td></tr>
<tr><td>行业</td><td>全球半导体赛道9家</td><td><a href="../research/semiconductor-sector-deep-dive-2026-05/">→</a></td></tr>
<tr><td>组合</td><td>AI智能体20成长股</td><td><a href="../research/ai-agent-20-portfolio-2026-05/">→</a></td></tr>
<tr><td>组合</td><td>国产算力10股</td><td><a href="../research/domestic-computing-10-portfolio-2026-05/">→</a></td></tr>
<tr><td>组合</td><td>红利组合</td><td><a href="../research/dividend-portfolio-2026-05/">→</a></td></tr>
<tr><td>宏观</td><td>2026年5月宏观快报</td><td><a href="../research/macro-briefing-2026-05/">→</a></td></tr>
</tbody>
</table>
</div>

</div>

<div class="tl-stats">
  <div class="tl-stat">
    <div class="tl-stat-num">4</div>
    <div class="tl-stat-label">宏观快报</div>
  </div>
  <div class="tl-stat">
    <div class="tl-stat-num">6</div>
    <div class="tl-stat-label">行业分析</div>
  </div>
  <div class="tl-stat">
    <div class="tl-stat-num">4</div>
    <div class="tl-stat-label">投资组合</div>
  </div>
  <div class="tl-stat">
    <div class="tl-stat-num">15</div>
    <div class="tl-stat-label">个股深度</div>
  </div>
  <div class="tl-stat">
    <div class="tl-stat-num">3</div>
    <div class="tl-stat-label">事件分析</div>
  </div>
  <div class="tl-stat">
    <div class="tl-stat-num">3</div>
    <div class="tl-stat-label">策略框架</div>
  </div>
</div>

</div>

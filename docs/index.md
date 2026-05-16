<style>
  .idx-wrapper {
    --gold: #c9a95c;
    --gold-bright: #e0c878;
    --steel: #4a90d9;
    --steel-bright: #64b5f6;
    --ice: #e8edf2;
    --ice-dim: #b0bec5;
    max-width: 900px;
    margin: 0 auto;
  }

  .idx-hero {
    padding: 36px 0 28px;
    border-bottom: 1px solid rgba(74,144,217,0.1);
    margin-bottom: 32px;
    animation: idxFadeUp 0.6s ease;
  }
  .idx-hero-tag {
    font-size: 10px;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 10px;
  }
  .idx-hero h1 {
    font-family: Georgia, 'Noto Serif SC', serif !important;
    font-size: 54px !important;
    font-weight: 400 !important;
    color: var(--ice) !important;
    line-height: 1.15 !important;
    letter-spacing: -0.03em !important;
    border: none !important;
    padding: 0 !important;
    margin: 0 0 8px 0 !important;
  }
  .idx-hero-sub {

  /* 最新研究模块 */
  .idx-latest {
    margin: 0 0 28px;
    animation: idxFadeUp 0.6s ease 0.1s both;
  }
  .idx-latest-label {
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 10px;
  }
  .idx-latest-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }
  .idx-latest-card {
    background: rgba(74,144,217,0.05);
    border: 1px solid rgba(74,144,217,0.10);
    border-radius: 4px;
    padding: 14px 16px;
    transition: background 0.2s;
    text-decoration: none;
    display: block;
  }
  .idx-latest-card:hover {
    background: rgba(74,144,217,0.10);
    border-color: rgba(74,144,217,0.20);
  }
  .idx-latest-card-tag {
    font-size: 9px;
    letter-spacing: 0.1em;
    color: var(--gold);
    margin-bottom: 4px;
  }
  .idx-latest-card h4 {
    font-size: 13px;
    font-weight: 600;
    color: var(--ice) !important;
    margin: 0 0 4px;
    line-height: 1.3;
    border: none !important;
    padding: 0 !important;
  }
  .idx-latest-card p {
    font-size: 10px;
    color: var(--ice-dim);
    margin: 0;
    line-height: 1.4;
  }
  @media (max-width: 768px) {
    .idx-latest-row { grid-template-columns: 1fr; }
  }
    font-size: 15px;
    color: var(--ice-dim);
    letter-spacing: 0.01em;
  }

  .idx-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: rgba(74,144,217,0.08);
    border: 1px solid rgba(74,144,217,0.1);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 36px;
    animation: idxFadeUp 0.6s ease 0.1s both;
  }
  .idx-stat {
    background: rgba(13,31,53,0.5);
    padding: 22px 16px;
    text-align: center;
    transition: background 0.2s;
  }
  .idx-stat:hover { background: rgba(17,40,64,0.7); }
  .idx-stat-num {
    font-family: Georgia, serif;
    font-size: 32px;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 4px;
  }
  .idx-stat-label {
    font-size: 10px;
    color: var(--ice-dim);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .idx-section-title {
    font-family: Georgia, 'Noto Serif SC', serif;
    font-size: 19px;
    font-weight: 400;
    color: var(--ice);
    margin: 36px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    animation: idxFadeUp 0.6s ease both;
  }
  .idx-section-title::before {
    content: '';
    display: inline-block;
    width: 7px; height: 7px;
    background: var(--gold);
    transform: rotate(45deg);
    flex-shrink: 0;
  }

  .idx-philosophy {
    background: rgba(74,144,217,0.03);
    border-left: 2px solid var(--gold);
    padding: 20px 24px;
    margin-bottom: 32px;
    border-radius: 0 4px 4px 0;
    animation: idxFadeUp 0.6s ease 0.12s both;
  }
  .idx-philosophy p {
    font-size: 14px;
    line-height: 1.8;
    color: var(--ice-dim);
    margin: 0;
    font-style: italic;
  }
  .idx-philosophy .attribution {
    font-size: 11px;
    color: #8a7038;
    margin-top: 6px;
    font-style: normal;
    letter-spacing: 0.04em;
  }

  .idx-coverage {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 32px;
    animation: idxFadeUp 0.6s ease 0.18s both;
  }
  .idx-cov-card {
    background: rgba(13,31,53,0.5);
    border: 1px solid rgba(74,144,217,0.07);
    border-radius: 4px;
    padding: 18px;
    transition: border-color 0.2s, transform 0.2s;
  }
  .idx-cov-card:hover {
    border-color: rgba(74,144,217,0.25);
    transform: translateY(-2px);
  }
  .idx-cov-icon {
    font-size: 18px;
    margin-bottom: 8px;
    opacity: 0.6;
  }
  .idx-cov-label {
    font-size: 11px;
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 6px;
  }
  .idx-cov-body {
    font-size: 12px;
    color: var(--ice-dim);
    line-height: 1.6;
  }

  .idx-models {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin-bottom: 36px;
    animation: idxFadeUp 0.6s ease 0.24s both;
  }
  .idx-model {
    display: flex;
    gap: 10px;
    padding: 14px 16px;
    background: rgba(13,31,53,0.4);
    border: 1px solid rgba(74,144,217,0.05);
    border-radius: 4px;
    transition: border-color 0.2s;
  }
  .idx-model:hover { border-color: rgba(201,169,92,0.2); }
  .idx-model-icon {
    flex-shrink: 0;
    width: 26px; height: 26px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(201,169,92,0.08);
    border-radius: 2px;
    font-size: 12px;
    color: var(--gold);
  }
  .idx-model-body h4 {
    font-size: 12px;
    color: var(--ice);
    font-weight: 600;
    margin: 0 0 2px;
    text-transform: none;
    letter-spacing: 0;
  }
  .idx-model-body p {
    font-size: 11px;
    color: var(--ice-dim);
    line-height: 1.45;
    margin: 0;
  }

  .idx-declare {
    padding: 18px 24px;
    border: 1px dashed rgba(74,144,217,0.12);
    border-radius: 4px;
    text-align: center;
    margin-bottom: 32px;
    animation: idxFadeUp 0.6s ease 0.3s both;
  }
  .idx-declare p {
    font-size: 12px;
    color: #5c6e84;
    margin: 0;
    line-height: 1.7;
  }

  .idx-game-link {
    text-align: center;
    padding: 16px;
    background: rgba(13,31,53,0.4);
    border: 1px solid rgba(74,144,217,0.07);
    border-radius: 4px;
    animation: idxFadeUp 0.6s ease 0.35s both;
    transition: border-color 0.2s;
  }
  .idx-game-link:hover { border-color: rgba(74,144,217,0.25); }
  .idx-game-link a {
    font-size: 13px;
    color: var(--steel-bright) !important;
    border: none !important;
  }

  @keyframes idxFadeUp {
    from { opacity: 0; transform: translateY(16px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @media (max-width: 768px) {
    .idx-hero h1 { font-size: 34px !important; }
    .idx-stats { grid-template-columns: repeat(2, 1fr); }
    .idx-coverage { grid-template-columns: 1fr; }
    .idx-models { grid-template-columns: 1fr; }
  }
</style>

<div class="idx-wrapper">

<div class="idx-hero">
  <div class="idx-hero-tag">The Rigorous Investor</div>
  <h1>投资严论</h1>
  <div class="idx-hero-sub">多资产长期价值投资独立研究</div>
</div>

<div class="idx-latest">
  <div class="idx-latest-label">最新研究</div>
  <div class="idx-latest-row">
    <a class="idx-latest-card" href="research/eight-dimension-framework/">
      <div class="idx-latest-card-tag">策略框架 · 5月17日</div>
      <h4>八维投资分析体系</h4>
      <p>商业模式→护城河→竞争→周期→估值→管理层→Pre-mortem</p>
    </a>
    <a class="idx-latest-card" href="research/macro-dashboard-2026-05/">
      <div class="idx-latest-card-tag">宏观快报 · 5月17日</div>
      <h4>宏观仪表盘（5月）</h4>
      <p>中美35项核心指标一览 · 三滤镜🟡谨慎中性</p>
    </a>
    <a class="idx-latest-card" href="research/s-curve-timing-system-2026-05/">
      <div class="idx-latest-card-tag">策略框架 · 5月17日</div>
      <h4>渗透率 S 曲线择时体系</h4>
      <p>甜蜜区5%→30% · 七大当前赛道定位</p>
    </a>
  </div>
</div>

<div class="idx-stats">
  <div class="idx-stat">
    <div class="idx-stat-num">44</div>
    <div class="idx-stat-label">深度研报</div>
  </div>
  <div class="idx-stat">
    <div class="idx-stat-num">50+</div>
    <div class="idx-stat-label">覆盖标的</div>
  </div>
  <div class="idx-stat">
    <div class="idx-stat-num">5</div>
    <div class="idx-stat-label">研究赛道</div>
  </div>
  <div class="idx-stat">
    <div class="idx-stat-num">8</div>
    <div class="idx-stat-label">分析维度</div>
  </div>
</div>

<div class="idx-section-title">投资哲学</div>

<div class="idx-philosophy">
  <p>"手里拿着锤子的人，看什么都像钉子。聪明人为什么会犯错？因为他们没有把所有的核心思维模型——来自多个学科的重大思想——都列成清单来用。"</p>
  <p class="attribution">—— 查理·芒格</p>
</div>

<p style="font-size:14px;color:var(--ice-dim);line-height:1.8;margin-bottom:24px;">
遵循<b style="color:var(--ice)">芒格多元思维模型</b>与<b style="color:var(--ice)">巴菲特价值投资</b>理念。
运用心理学、经济学、工程学、生物学多学科视角理解商业本质。
寻找有深厚护城河的优质企业，以合理价格买入并长期持有。
<b style="color:#c9a95c">反过来想，总是反过来想</b>——每笔投资先假设它会归零。
</p>

<div class="idx-section-title">研究覆盖</div>

<div class="idx-coverage">
  <div class="idx-cov-card">
    <div class="idx-cov-icon">◆</div>
    <div class="idx-cov-label">宏观快报</div>
    <div class="idx-cov-body">中美利差 · 汇率 · 全球流动性 · 关税/出口管制 —— 每季度更新</div>
  </div>
  <div class="idx-cov-card">
    <div class="idx-cov-icon">◈</div>
    <div class="idx-cov-label">行业分析</div>
    <div class="idx-cov-body">半导体赛道 · 存储产业链 · 国产GPU · CPU周期 · ETF对比</div>
  </div>
  <div class="idx-cov-card">
    <div class="idx-cov-icon">⟐</div>
    <div class="idx-cov-label">投资组合</div>
    <div class="idx-cov-body">AI智能体20股 · 国产算力10股 · 红利组合10只</div>
  </div>
  <div class="idx-cov-card">
    <div class="idx-cov-icon">◎</div>
    <div class="idx-cov-label">个股深度</div>
    <div class="idx-cov-body">NVDA · TSM · GOOGL · MU · 茅台 · 海光 · 中芯 · 三星等 16 篇</div>
  </div>
  <div class="idx-cov-card">
    <div class="idx-cov-icon">⟲</div>
    <div class="idx-cov-label">事件分析</div>
    <div class="idx-cov-body">巴菲特股东大会 2026 · 更多事件驱动研究</div>
  </div>
  <div class="idx-cov-card">
    <div class="idx-cov-icon">◉</div>
    <div class="idx-cov-label">数据工具</div>
    <div class="idx-cov-body">Python 量化分析 · ETF 绩效对比 · 相关性矩阵 · 回测引擎</div>
  </div>
</div>

<div class="idx-section-title">芒格思维模型实践</div>

<div class="idx-models">
  <div class="idx-model">
    <div class="idx-model-icon">⟲</div>
    <div class="idx-model-body">
      <h4>逆向思维</h4>
      <p>Pre-mortem：假设3年后归零</p>
    </div>
  </div>
  <div class="idx-model">
    <div class="idx-model-icon">⟐</div>
    <div class="idx-model-body">
      <h4>误判心理学</h4>
      <p>确认偏误 · 叙事谬误防御</p>
    </div>
  </div>
  <div class="idx-model">
    <div class="idx-model-icon">◈</div>
    <div class="idx-model-body">
      <h4>生态系统分析</h4>
      <p>护城河 + 竞争 + 周期三维透视</p>
    </div>
  </div>
  <div class="idx-model">
    <div class="idx-model-icon">◆</div>
    <div class="idx-model-body">
      <h4>安全边际</h4>
      <p>双方法估值交叉验证</p>
    </div>
  </div>
  <div class="idx-model">
    <div class="idx-model-icon">◉</div>
    <div class="idx-model-body">
      <h4>能力圈</h4>
      <p>只研究可理解的商业模式</p>
    </div>
  </div>
  <div class="idx-model">
    <div class="idx-model-icon">◎</div>
    <div class="idx-model-body">
      <h4>复利思维</h4>
      <p>5年以上长周期累积效应</p>
    </div>
  </div>
</div>

<div class="idx-declare">
  <p>本站所有内容仅供个人投资研究参考，<b style="color:#e0c878">不构成投资建议</b>。研究框架学习自查理·芒格的多元思维模型理论，错误和偏见归研究者本人。</p>
</div>

<div class="idx-game-link">
  <a href="games/snake/">贪吃蛇 — 经典街机小游戏，手机触屏也能玩</a>
</div>

</div>

<style>
  /* ===== 关于本站 · 定制样式 ===== */
  .about-wrapper {
    --gold: #c9a95c;
    --gold-bright: #e0c878;
    --gold-dim: #8a7038;
    --steel: #4a90d9;
    --steel-bright: #64b5f6;
    --navy-900: #0a1628;
    --navy-800: #0d1f35;
    --navy-700: #112840;
    --navy-600: #163553;
    --ice: #e8edf2;
    --ice-dim: #b0bec5;
    max-width: 860px;
    margin: 0 auto;
  }

  /* Hero */
  .about-hero {
    padding: 48px 0 32px;
    border-bottom: 1px solid rgba(74,144,217,0.12);
    margin-bottom: 40px;
    animation: aboutFadeUp 0.7s ease;
  }
  .about-hero-tag {
    font-size: 10px;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 12px;
  }
  .about-hero h1 {
    font-family: Georgia, 'Noto Serif SC', 'Songti SC', serif;
    font-size: 56px;
    font-weight: 400;
    color: var(--ice) !important;
    line-height: 1.15;
    letter-spacing: -0.025em;
    border: none !important;
    padding: 0 !important;
    margin: 0 0 12px 0 !important;
  }
  .about-hero-sub {
    font-size: 15px;
    color: var(--ice-dim);
    letter-spacing: 0.02em;
  }

  /* Stat Cards Row */
  .about-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: rgba(74,144,217,0.08);
    border: 1px solid rgba(74,144,217,0.1);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 48px;
    animation: aboutFadeUp 0.7s ease 0.1s both;
  }
  .about-stat {
    background: rgba(13,31,53,0.6);
    padding: 24px 20px;
    text-align: center;
    position: relative;
    transition: background 0.25s;
  }
  .about-stat:hover {
    background: rgba(17,40,64,0.8);
  }
  .about-stat-num {
    font-family: Georgia, serif;
    font-size: 36px;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 6px;
  }
  .about-stat-label {
    font-size: 11px;
    color: var(--ice-dim);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  /* Section Title */
  .about-section-title {
    font-family: Georgia, 'Noto Serif SC', serif;
    font-size: 20px;
    font-weight: 400;
    color: var(--ice);
    margin: 40px 0 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    animation: aboutFadeUp 0.7s ease both;
  }
  .about-section-title::before {
    content: '';
    display: inline-block;
    width: 7px; height: 7px;
    background: var(--gold);
    transform: rotate(45deg);
    flex-shrink: 0;
  }

  /* Philosophy Blockquote */
  .about-philosophy {
    background: rgba(74,144,217,0.04);
    border-left: 2px solid var(--gold);
    padding: 24px 28px;
    margin: 20px 0 36px;
    border-radius: 0 4px 4px 0;
    animation: aboutFadeUp 0.7s ease 0.15s both;
  }
  .about-philosophy p {
    font-size: 15px;
    line-height: 1.85;
    color: var(--ice);
    margin: 0;
  }
  .about-philosophy .attribution {
    font-size: 12px;
    color: var(--gold-dim);
    margin-top: 8px;
    letter-spacing: 0.05em;
  }

  /* Framework Cards */
  .about-framework {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 36px;
    animation: aboutFadeUp 0.7s ease 0.2s both;
  }
  .about-fw-card {
    background: rgba(13,31,53,0.5);
    border: 1px solid rgba(74,144,217,0.08);
    border-radius: 4px;
    padding: 20px;
    transition: border-color 0.25s, transform 0.25s;
  }
  .about-fw-card:hover {
    border-color: rgba(74,144,217,0.3);
    transform: translateY(-2px);
  }
  .about-fw-num {
    font-family: Georgia, serif;
    font-size: 32px;
    color: var(--steel);
    opacity: 0.35;
    line-height: 1;
    margin-bottom: 8px;
  }
  .about-fw-label {
    font-size: 13px;
    color: var(--ice);
    font-weight: 600;
    margin-bottom: 4px;
  }
  .about-fw-desc {
    font-size: 11px;
    color: var(--ice-dim);
    line-height: 1.5;
  }

  /* Research Coverage Map */
  .about-coverage {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: rgba(74,144,217,0.08);
    border: 1px solid rgba(74,144,217,0.1);
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 36px;
    animation: aboutFadeUp 0.7s ease 0.25s both;
  }
  .about-cov-item {
    background: rgba(13,31,53,0.6);
    padding: 20px;
  }
  .about-cov-label {
    font-size: 10px;
    color: var(--gold);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    margin-bottom: 8px;
  }
  .about-cov-stocks {
    font-size: 12px;
    color: var(--ice-dim);
    line-height: 1.7;
  }

  /* Mental Model Grid */
  .about-models {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 48px;
    animation: aboutFadeUp 0.7s ease 0.3s both;
  }
  .about-model {
    display: flex;
    gap: 14px;
    padding: 16px 18px;
    background: rgba(13,31,53,0.5);
    border: 1px solid rgba(74,144,217,0.06);
    border-radius: 4px;
    transition: border-color 0.25s;
  }
  .about-model:hover {
    border-color: rgba(201,169,92,0.25);
  }
  .about-model-icon {
    flex-shrink: 0;
    width: 32px; height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(201,169,92,0.1);
    border-radius: 2px;
    font-size: 14px;
    color: var(--gold);
  }
  .about-model-body h4 {
    font-size: 13px;
    color: var(--ice);
    font-weight: 600;
    margin: 0 0 3px;
  }
  .about-model-body p {
    font-size: 11px;
    color: var(--ice-dim);
    line-height: 1.5;
    margin: 0;
  }

  /* Disclaimer */
  .about-disclaimer {
    padding: 20px 24px;
    border: 1px dashed rgba(74,144,217,0.15);
    border-radius: 4px;
    text-align: center;
    margin: 48px 0 24px;
    animation: aboutFadeUp 0.7s ease 0.4s both;
  }
  .about-disclaimer p {
    font-size: 12px;
    color: #5c6e84;
    margin: 0;
    line-height: 1.7;
  }

  /* Animations */
  @keyframes aboutFadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Responsive */
  @media (max-width: 768px) {
    .about-hero h1 { font-size: 36px; }
    .about-stats { grid-template-columns: repeat(2, 1fr); }
    .about-framework { grid-template-columns: repeat(2, 1fr); }
    .about-coverage { grid-template-columns: 1fr; }
    .about-models { grid-template-columns: 1fr; }
  }
</style>

<div class="about-wrapper">

<!-- Hero -->
<div class="about-hero">
  <div class="about-hero-tag">The Rigorous Investor</div>
  <h1>投资严论</h1>
  <div class="about-hero-sub">多资产长期价值投资独立研究 · 遵循芒格与巴菲特的智慧</div>
</div>

<!-- Stats -->
<div class="about-stats">
  <div class="about-stat">
    <div class="about-stat-num">24</div>
    <div class="about-stat-label">深度研报</div>
  </div>
  <div class="about-stat">
    <div class="about-stat-num">30+</div>
    <div class="about-stat-label">覆盖标的</div>
  </div>
  <div class="about-stat">
    <div class="about-stat-num">5</div>
    <div class="about-stat-label">研究赛道</div>
  </div>
  <div class="about-stat">
    <div class="about-stat-num">8</div>
    <div class="about-stat-label">分析维度</div>
  </div>
</div>

<!-- Philosophy -->
<div class="about-section-title">投资哲学</div>

<div class="about-philosophy">
  <p>"手里拿着锤子的人，看什么都像钉子。聪明人为什么会犯错？因为他们没有把所有的核心思维模型——来自多个学科的重大思想——都列成清单来用。"</p>
  <p class="attribution">—— 查理·芒格</p>
</div>

<p style="color:var(--ice-dim);font-size:14px;line-height:1.8;margin-bottom:20px;">
本站遵循芒格的<b style="color:var(--ice)">多元思维模型</b>与巴菲特的<b style="color:var(--ice)">价值投资理念</b>。
运用心理学、经济学、工程学、生物学多学科视角理解商业本质。
寻找有深厚护城河的优质企业，以合理价格买入并长期持有。
<b style="color:var(--gold)">反过来想，总是反过来想</b>——每笔投资先假设它会归零，找出最可能的死因。
</p>

<!-- Framework -->
<div class="about-section-title">分析框架</div>

<div class="about-framework">
  <div class="about-fw-card">
    <div class="about-fw-num">01</div>
    <div class="about-fw-label">商业模式</div>
    <div class="about-fw-desc">收入结构、客户粘性、单位经济模型</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">02</div>
    <div class="about-fw-label">护城河</div>
    <div class="about-fw-desc">壁垒宽度、趋势方向、替代威胁</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">03</div>
    <div class="about-fw-label">竞争格局</div>
    <div class="about-fw-desc">行业份额、新进入者、五力分析</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">04</div>
    <div class="about-fw-label">行业周期</div>
    <div class="about-fw-desc">周期位置、供需关系、产能变化</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">05</div>
    <div class="about-fw-label">催化剂与风险</div>
    <div class="about-fw-desc">未来1-3年关键变量与概率评估</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">06</div>
    <div class="about-fw-label">估值</div>
    <div class="about-fw-desc">DCF + 可比估值双重交叉验证</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">07</div>
    <div class="about-fw-label">管理层与治理</div>
    <div class="about-fw-desc">资本配置能力、诚信、股权结构</div>
  </div>
  <div class="about-fw-card">
    <div class="about-fw-num">08</div>
    <div class="about-fw-label">逆向验证</div>
    <div class="about-fw-desc">假设3年后归零，最可能的死因？</div>
  </div>
</div>

<!-- Coverage -->
<div class="about-section-title">研究覆盖</div>

<div class="about-coverage">
  <div class="about-cov-item">
    <div class="about-cov-label">美股</div>
    <div class="about-cov-stocks">NVDA · TSM · GOOGL · MU · SNDK · 16只AI智能体组合</div>
  </div>
  <div class="about-cov-item">
    <div class="about-cov-label">A股</div>
    <div class="about-cov-stocks">茅台 600519 · 海光 688041 · 摩尔线程 688795 · 中际旭创 300308 · 澜起 688008 · 国产算力10股</div>
  </div>
  <div class="about-cov-item">
    <div class="about-cov-label">港股 / 韩股 / 台股</div>
    <div class="about-cov-stocks">中芯国际 0981 · 华虹 1347 · 阿里 9988 · 三星 005930 · SK海力士 000660</div>
  </div>
  <div class="about-cov-item">
    <div class="about-cov-label">行业全景</div>
    <div class="about-cov-stocks">半导体赛道9家 · 存储产业链30+ · 国产GPU 11家 · CPU涨价周期</div>
  </div>
  <div class="about-cov-item">
    <div class="about-cov-label">宏观跟踪</div>
    <div class="about-cov-stocks">中美利差 · 汇率 · 流动性 · 关税/出口管制 · 每季度更新</div>
  </div>
  <div class="about-cov-item">
    <div class="about-cov-label">事件研究</div>
    <div class="about-cov-stocks">巴菲特股东大会 2026 · 更多事件驱动分析</div>
  </div>
</div>

<!-- Mental Models -->
<div class="about-section-title">芒格思维模型实践</div>

<div class="about-models">
  <div class="about-model">
    <div class="about-model-icon">⟲</div>
    <div class="about-model-body">
      <h4>逆向思维</h4>
      <p>Pre-mortem：假设3年后投资归零，找出最可能的死因并正面回应</p>
    </div>
  </div>
  <div class="about-model">
    <div class="about-model-icon">⟐</div>
    <div class="about-model-body">
      <h4>误判心理学</h4>
      <p>识别确认偏误、近期偏差、叙事谬误；内置反向验证机制</p>
    </div>
  </div>
  <div class="about-model">
    <div class="about-model-icon">◈</div>
    <div class="about-model-body">
      <h4>生态系统分析</h4>
      <p>护城河 + 竞争对手 + 行业周期三维分析，理解企业生态位</p>
    </div>
  </div>
  <div class="about-model">
    <div class="about-model-icon">◆</div>
    <div class="about-model-body">
      <h4>安全边际</h4>
      <p>估值用至少两种方法交叉验证，合理买入区间留有足够折扣</p>
    </div>
  </div>
  <div class="about-model">
    <div class="about-model-icon">◉</div>
    <div class="about-model-body">
      <h4>能力圈</h4>
      <p>只研究能理解的商业模式，赛道集中度超50%自动预警</p>
    </div>
  </div>
  <div class="about-model">
    <div class="about-model-icon">◎</div>
    <div class="about-model-body">
      <h4>复利思维</h4>
      <p>分红再投资长周期回测，关注5年以上累积效应而非短期波动</p>
    </div>
  </div>
</div>

<!-- Disclaimer -->
<div class="about-disclaimer">
  <p>本站所有内容仅供个人投资研究参考，<b style="color:#e0c878">不构成任何投资建议</b>。市场有风险，投资需谨慎。<br>作者可能持有或不持有所讨论的标的。研究框架学习自查理·芒格的多元思维模型理论，错误和偏见归研究者本人。</p>
</div>

</div>

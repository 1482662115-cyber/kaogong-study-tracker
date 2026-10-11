(function() {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim();
  var accent2 = style.getPropertyValue('--accent2').trim();
  var ink = style.getPropertyValue('--ink').trim();
  var muted = style.getPropertyValue('--muted').trim();
  var rule = style.getPropertyValue('--rule').trim();
  var bg2 = style.getPropertyValue('--bg2').trim();
  var red = style.getPropertyValue('--accent-red').trim();
  var amber = style.getPropertyValue('--accent-amber').trim();

  // ========== 数据 ==========
  var moduleData = [
    { name: '常识判断', total: 60, wrong: 33, correctRate: 45.0 },
    { name: '言语理解', total: 75, wrong: 19, correctRate: 74.7 },
    { name: '判断推理', total: 75, wrong: 29, correctRate: 61.3 },
    { name: '数量分析', total: 45, wrong: 16, correctRate: 64.4 },
    { name: '综合分析', total: 15, wrong: 10, correctRate: 33.3 }
  ];

  var subtypeData = [
    { module: '判断推理', type: '图形推理', total: 15, wrong: 7, rate: 53 },
    { module: '判断推理', type: '逻辑判断', total: 30, wrong: 14, rate: 53 },
    { module: '综合分析', type: '论证评价', total: 8, wrong: 6, rate: 25 },
    { module: '数量分析', type: '数学运算', total: 15, wrong: 10, rate: 33 },
    { module: '言语理解', type: '逻辑填空', total: 30, wrong: 10, rate: 67 },
    { module: '言语理解', type: '语句填空', total: 6, wrong: 2, rate: 67 },
    { module: '言语理解', type: '标题选择', total: 3, wrong: 1, rate: 67 },
    { module: '数量分析', type: '资料分析', total: 30, wrong: 6, rate: 80 },
    { module: '言语理解', type: '中心理解', total: 16, wrong: 3, rate: 81 },
    { module: '言语理解', type: '细节判断', total: 5, wrong: 1, rate: 80 },
    { module: '判断推理', type: '定义判断', total: 30, wrong: 4, rate: 87 },
    { module: '判断推理', type: '类比推理', total: 30, wrong: 4, rate: 87 }
  ];

  var reasonData = [
    { name: '知识点不会', value: 52 },
    { name: '概念混淆', value: 49 },
    { name: '粗心', value: 8 }
  ];

  // ========== 图1：雷达图 ==========
  var radar = echarts.init(document.getElementById('chart-radar'), null, { renderer: 'svg' });
  radar.setOption({
    animation: false,
    tooltip: { appendToBody: true, formatter: '{b}: {c}% 正确率' },
    radar: {
      indicator: moduleData.map(function(m) { return { name: m.name, max: 100 }; }),
      shape: 'polygon',
      splitNumber: 5,
      axisName: { color: muted, fontSize: 13, fontWeight: 600 },
      splitLine: { lineStyle: { color: rule } },
      splitArea: { show: false },
      axisLine: { lineStyle: { color: rule } }
    },
    series: [{
      type: 'radar',
      data: [{
        value: moduleData.map(function(m) { return m.correctRate; }),
        name: '正确率',
        areaStyle: {
          color: {
            type: 'linear', x: 0, y: 0, x2: 1, y2: 1,
            colorStops: [
              { offset: 0, color: accent + '55' },
              { offset: 1, color: accent2 + '55' }
            ]
          }
        },
        lineStyle: { color: accent, width: 2 },
        itemStyle: { color: accent, borderColor: bg2, borderWidth: 2 }
      }]
    }]
  });
  window.addEventListener('resize', function() { radar.resize(); });

  // ========== 图2：模块错题数条形图 ==========
  var bar = echarts.init(document.getElementById('chart-bar'), null, { renderer: 'svg' });
  var sorted = moduleData.slice().sort(function(a, b) { return b.wrong - a.wrong; });
  bar.setOption({
    animation: false,
    tooltip: { appendToBody: true, formatter: function(p) {
      var m = sorted[p.dataIndex];
      return m.name + '<br/>错题：' + m.wrong + '道 (正确率 ' + m.correctRate + '%)';
    }},
    grid: { left: 100, right: 30, top: 20, bottom: 30 },
    xAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: rule } },
      axisTick: { show: false },
      splitLine: { lineStyle: { color: rule, type: 'dashed' } },
      axisLabel: { color: muted }
    },
    yAxis: {
      type: 'category',
      data: sorted.map(function(m) { return m.name; }),
      axisLine: { lineStyle: { color: rule } },
      axisTick: { show: false },
      axisLabel: { color: ink, fontWeight: 600 }
    },
    series: [{
      type: 'bar',
      data: sorted.map(function(m) {
        var color = m.wrong > 25 ? red : m.wrong > 15 ? amber : accent2;
        return { value: m.wrong, itemStyle: { color: color, borderRadius: [0, 4, 4, 0] } };
      }),
      barWidth: 18,
      label: {
        show: true, position: 'right',
        formatter: function(p) { return p.value + ' 道'; },
        color: ink, fontSize: 12, fontWeight: 600
      }
    }]
  });
  window.addEventListener('resize', function() { bar.resize(); });

  // ========== 图3：细分题型正确率排行 ==========
  var subtypeChart = echarts.init(document.getElementById('chart-subtype'), null, { renderer: 'svg' });
  var subSorted = subtypeData.slice().sort(function(a, b) { return a.rate - b.rate; });
  subtypeChart.setOption({
    animation: false,
    tooltip: { appendToBody: true, formatter: function(p) {
      var s = subSorted[p.dataIndex];
      return s.module + ' · ' + s.type + '<br/>' + s.total + '题 / 错' + s.wrong + '道<br/>正确率: ' + s.rate + '%';
    }},
    grid: { left: 140, right: 50, top: 20, bottom: 30 },
    xAxis: {
      type: 'value', max: 100,
      axisLine: { lineStyle: { color: rule } },
      axisTick: { show: false },
      splitLine: { lineStyle: { color: rule, type: 'dashed' } },
      axisLabel: { color: muted, formatter: '{value}%' }
    },
    yAxis: {
      type: 'category',
      data: subSorted.map(function(s) { return s.type; }),
      axisLine: { lineStyle: { color: rule } },
      axisTick: { show: false },
      axisLabel: { color: ink, fontWeight: 600 }
    },
    series: [{
      type: 'bar',
      data: subSorted.map(function(s) {
        var c = s.rate < 40 ? red : s.rate < 70 ? amber : accent2;
        return {
          value: s.rate,
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
              { offset: 0, color: c + '33' },
              { offset: 1, color: c }
            ]),
            borderRadius: [0, 4, 4, 0]
          }
        };
      }),
      barWidth: 16,
      label: {
        show: true, position: 'right',
        formatter: function(p) { return p.value + '%'; },
        color: ink, fontSize: 12, fontWeight: 600
      },
      markLine: {
        silent: true,
        symbol: 'none',
        lineStyle: { color: rule, type: 'dashed' },
        data: [{ xAxis: 60, label: { formatter: '60% 警戒线', color: muted, position: 'end' } }]
      }
    }]
  });
  window.addEventListener('resize', function() { subtypeChart.resize(); });

  // ========== 图4：错因饼图 ==========
  var pie = echarts.init(document.getElementById('chart-reason'), null, { renderer: 'svg' });
  pie.setOption({
    animation: false,
    tooltip: { appendToBody: true, formatter: '{b}: {c}题 ({d}%)' },
    legend: {
      bottom: 0, left: 'center',
      textStyle: { color: ink, fontSize: 12 },
      itemWidth: 12, itemHeight: 12
    },
    color: [accent, amber, red],
    series: [{
      type: 'pie',
      radius: ['45%', '70%'],
      center: ['50%', '42%'],
      data: reasonData,
      itemStyle: { borderColor: bg2, borderWidth: 3, borderRadius: 4 },
      label: { show: false },
      emphasis: {
        label: { show: true, formatter: '{d}%', fontSize: 18, fontWeight: 700, color: ink }
      }
    }]
  });
  window.addEventListener('resize', function() { pie.resize(); });

  // ========== 动态填充表格 ==========
  var tbody = document.getElementById('tbody-subtype');
  if (tbody) {
    var sortedForTable = subtypeData.slice().sort(function(a, b) { return a.rate - b.rate; });
    sortedForTable.forEach(function(s) {
      var tag, cls;
      if (s.rate < 40) { tag = '🔴 重灾区'; cls = 'tag-red'; }
      else if (s.rate < 60) { tag = '🟠 薄弱'; cls = 'tag-red'; }
      else if (s.rate < 80) { tag = '🟡 待提升'; cls = 'tag-amber'; }
      else { tag = '🟢 稳定'; cls = 'tag-green'; }

      var rateCls = s.rate >= 80 ? 'rate-high' : s.rate >= 60 ? 'rate-mid' : 'rate-low';

      var tr = document.createElement('tr');
      tr.innerHTML =
        '<td>' + s.module + '</td>' +
        '<td>' + s.type + '</td>' +
        '<td>' + s.total + '</td>' +
        '<td style="color:' + red + ';font-weight:600;">' + s.wrong + '</td>' +
        '<td class="' + rateCls + '">' + s.rate + '%</td>' +
        '<td><span class="tag ' + cls + '">' + tag + '</span></td>';
      tbody.appendChild(tr);
    });
  }
})();

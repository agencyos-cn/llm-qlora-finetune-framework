# 提交规范

## 提交消息格式

每个提交消息都应该遵循以下格式：

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

其中 `<type>` 和 `<subject>` 是必需的， `<scope>` 和 `<body>` 是可选的。

## 类型 (Type)

提交类型必须是以下之一：

- `build`: 影响构建系统或外部依赖项的更改（例如：gulp，broccoli，npm）
- `ci`: 更改CI配置文件和脚本（例如：Travis，Circle，BrowserStack，SauceLabs）
- `docs`: 文档的仅限更改
- `feat`: 新功能
- `fix`: 修复错误
- `perf`: 提高性能的代码更改
- `refactor`: 既不修复错误也不添加功能的代码更改
- `style`: 不影响代码含义的更改（空白、格式化、缺少分号等）
- `test`: 添加缺失测试或更正现有测试

## 范围 (Scope)

范围应该是描述更改所影响部分的小名词，例如：`config`, `loader`, `model`, `controller`, `view`, `route` 等。

## 主题 (Subject)

主题应该使用祈使语气，简明扼要地描述更改。它不应该大写，也不应该以句号结尾。

## 正文 (Body)

正文应该包含更改的动机和对比，描述做了什么以及为什么。

## 脚注 (Footer)

脚注应该包含任何中断性更改，以及对问题或PR的引用。

## 示例

```
feat(config): 添加模型验证选项

- 添加validateSchema选项以允许定义模型验证
- 更新文档以反映此更改

Fixes #123
BREAKING CHANGE: 旧的配置格式不再受支持
```

```
fix(model): 修复验证器未正确处理空值的问题

- 添加对null和undefined值的特殊处理
- 更新单元测试以包含边界情况

Refs #456
```

---

遵循这些约定有助于使项目历史记录更易于理解和搜索，也使得自动生成发布日志成为可能。
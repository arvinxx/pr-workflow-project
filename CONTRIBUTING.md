# 贡献指南 - PR工作流

## 🔄 开发流程

### 1. 准备工作
- Fork仓库到个人账户
- Clone到本地：`git clone https://github.com/your-username/pr-workflow-project.git`
- 添加上游仓库：`git remote add upstream https://github.com/arvinxx/pr-workflow-project.git`

### 2. 创建功能分支
```bash
git checkout -b feature/your-feature-name
# 或者
git checkout -b bugfix/fix-issue-number
```

### 3. 开发代码
- 编写代码
- 添加测试
- 更新文档

### 4. 提交代码
```bash
git add .
git commit -m "type(scope): description"
```

#### 提交信息规范
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 5. 推送并创建PR
```bash
git push origin feature/your-feature-name
```

然后在GitHub上创建Pull Request。

## 📋 PR检查清单

提交PR前请确保：

- [ ] 代码通过所有测试
- [ ] 添加了必要的测试用例
- [ ] 更新了相关文档
- [ ] 遵循代码规范
- [ ] PR描述清晰，关联了相关Issue

## 🔍 Code Review过程

1. **自动检查**：CI会自动运行测试和代码质量检查
2. **人工审查**：至少需要一名维护者审查
3. **反馈处理**：根据审查意见修改代码
4. **合并**：审查通过后合并到主分支

## 🚀 发布流程

- `main` 分支：生产环境
- `develop` 分支：开发环境
- `feature/*` 分支：功能开发
- `bugfix/*` 分支：bug修复
- `hotfix/*` 分支：紧急修复

# Contributing Guide

Thank you for your interest in contributing to the OLLAMA AI & OCR Agents project! This guide will help you get started.

## 🎯 Ways to Contribute

### 1. Bug Reports
- Check if the issue already exists
- Provide detailed reproduction steps
- Include system information (OS, Python version, OLLAMA version)
- Share error messages and logs

### 2. Feature Requests
- Describe the use case
- Explain expected behavior
- Suggest implementation approach if possible

### 3. Code Contributions
- Bug fixes
- New agent capabilities
- Performance improvements
- Documentation updates
- Example scripts

### 4. Documentation
- Improve existing docs
- Add tutorials and guides
- Create video demonstrations
- Translate documentation

### 5. Research
- Test different models
- Share performance benchmarks
- Document best practices
- Create case studies

## 🛠️ Development Setup

### 1. Fork and Clone
```bash
# Fork the repository on GitHub
git clone https://github.com/YOUR_USERNAME/Operations-using-Ollama-.git
cd Operations-using-Ollama-

# Add upstream remote
git remote add upstream https://github.com/suhaif314/Operations-using-Ollama-.git
```

### 2. Create Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Create Branch
```bash
# Create feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

## 📝 Code Style

### Python Guidelines
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add type hints where appropriate

### Example:
```python
def process_document(
    image_path: str,
    analyze: bool = True,
    analysis_type: str = "summary"
) -> Dict[str, Any]:
    """
    Process a document with OCR and optional AI analysis.
    
    Args:
        image_path: Path to the image file
        analyze: Whether to perform AI analysis
        analysis_type: Type of analysis ('summary', 'key_points', etc.)
        
    Returns:
        Dictionary containing processing results
    """
    # Implementation
    pass
```

## 🧪 Testing

### Before Submitting
1. Test your changes locally
2. Run syntax checks: `python -m py_compile your_file.py`
3. Test with different models if applicable
4. Test error handling
5. Update documentation

### Example Test
```python
# test_your_feature.py
from agents import AIAgent

def test_new_feature():
    agent = AIAgent()
    result = agent.new_feature("test input")
    assert result is not None
    print("✓ Test passed")

if __name__ == "__main__":
    test_new_feature()
```

## 📦 Pull Request Process

### 1. Commit Your Changes
```bash
# Stage changes
git add .

# Commit with clear message
git commit -m "Add: Brief description of changes"
# Use prefixes: Add, Fix, Update, Refactor, Docs
```

### 2. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request
- Go to GitHub and create a pull request
- Fill in the PR template
- Link related issues
- Request review

### PR Title Format
- `Add: New sentiment analysis feature`
- `Fix: OCR confidence calculation bug`
- `Update: Improve error handling in AIAgent`
- `Docs: Add tutorial for custom agents`

### PR Description Should Include
- What changes were made
- Why the changes are needed
- How to test the changes
- Any breaking changes
- Related issues

## 📋 Commit Message Guidelines

### Format
```
<type>: <subject>

<body>

<footer>
```

### Types
- **Add**: New feature or capability
- **Fix**: Bug fix
- **Update**: Update existing functionality
- **Refactor**: Code restructuring
- **Docs**: Documentation changes
- **Test**: Adding or updating tests
- **Chore**: Maintenance tasks

### Examples
```
Add: Multi-language OCR support

- Added language parameter to OCRAgent
- Updated preprocessing for non-English text
- Added examples for Spanish and French

Closes #123
```

## 🎨 Adding New Features

### For New Agent Capabilities
1. Add method to appropriate agent class
2. Include docstring with examples
3. Add corresponding example in examples/
4. Update README.md
5. Test thoroughly

### Example Structure
```python
# In agents/ai_agent.py
def new_capability(self, input_data: str) -> str:
    """
    Brief description of what this does.
    
    Args:
        input_data: Description
        
    Returns:
        Result description
        
    Example:
        >>> agent = AIAgent()
        >>> result = agent.new_capability("test")
        >>> print(result)
    """
    # Implementation
    pass
```

## 📚 Documentation

### What to Document
- All new features
- Breaking changes
- Configuration options
- Usage examples
- API changes

### Where to Document
- **README.md**: Main features and usage
- **QUICKSTART.md**: Getting started guide
- **RESEARCH_GUIDE.md**: Advanced topics
- **Docstrings**: In-code documentation
- **examples/**: Working code examples

## 🐛 Bug Fix Process

1. **Reproduce**: Confirm the bug exists
2. **Isolate**: Identify the root cause
3. **Fix**: Implement the solution
4. **Test**: Verify the fix works
5. **Document**: Update relevant docs
6. **Submit**: Create pull request

## ✅ Checklist Before Submitting

- [ ] Code follows style guidelines
- [ ] All files have appropriate docstrings
- [ ] Changes are tested locally
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No unnecessary files included
- [ ] Examples work correctly
- [ ] Breaking changes are documented

## 💡 Ideas for Contributions

### Easy (Good First Issues)
- Add more example scripts
- Improve error messages
- Add type hints
- Fix typos in documentation
- Add more comments

### Medium
- Add new agent methods
- Improve image preprocessing
- Add support for new document types
- Create tutorials
- Performance optimizations

### Advanced
- Implement multi-modal agents
- Add vector database integration
- Create specialized domain agents
- Build monitoring and logging
- Implement caching mechanisms

## 🤝 Code Review Process

### What We Look For
- Functionality: Does it work as intended?
- Code quality: Is it clean and maintainable?
- Documentation: Is it well documented?
- Testing: Is it properly tested?
- Performance: Does it maintain good performance?

### Review Timeline
- Initial review: Within 3-5 days
- Follow-up: Within 1-2 days
- Merge: After approval from maintainers

## 🔄 Staying Updated

### Sync Your Fork
```bash
# Fetch upstream changes
git fetch upstream

# Merge into your local branch
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

## 📞 Getting Help

- **Questions**: Open a discussion on GitHub
- **Bugs**: Open an issue with details
- **Features**: Open an issue with proposal
- **Chat**: Join community discussions

## 📜 Code of Conduct

### Be Respectful
- Use welcoming language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Be Professional
- Use appropriate language
- Stay on topic
- Provide constructive feedback
- Help others learn

## 🎉 Recognition

Contributors will be:
- Listed in the repository
- Credited in release notes
- Mentioned in documentation

Thank you for contributing! 🙏

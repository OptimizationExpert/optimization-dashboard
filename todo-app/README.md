# To-Do List Application

A modern, fully-featured to-do list application with local storage functionality, built with vanilla HTML, CSS, and JavaScript.

## ✨ Features

### Core Functionality
- ✅ **Add Tasks** - Create new to-do items easily
- ✅ **Mark Complete** - Check off finished tasks
- ✅ **Delete Tasks** - Remove individual items
- ✅ **Clear Completed** - Bulk remove all finished tasks
- ✅ **Filter Tasks** - View All, Active, or Completed tasks
- ✅ **Live Statistics** - Real-time counters (Total, Active, Completed)

### Storage & Persistence
- 💾 **Local Storage** - Tasks persist across browser sessions
- 📊 **Automatic Save** - Changes saved instantly
- 🔄 **Data Recovery** - Tasks restored on page reload

### User Experience
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- ⌨️ **Keyboard Support** - Press Enter to add tasks
- 🎯 **Task Timestamps** - Each task shows creation time
- 🔔 **Notifications** - User feedback for actions
- 🎪 **Empty States** - Helpful messages when no tasks exist

## 📁 File Structure

```
todo-app/
├── index.html      # HTML structure
├── styles.css      # Styling and animations
├── script.js       # JavaScript functionality
└── README.md       # This file
```

## 🚀 Quick Start

### Option 1: Open Locally
1. Download all files to a folder
2. Open `index.html` in your browser
3. Start adding tasks!

### Option 2: From Repository
```bash
# Clone the repository
git clone https://github.com/OptimizationExpert/optimization-dashboard.git

# Navigate to the app
cd optimization-dashboard/todo-app

# Open in browser
open index.html  # macOS
# or
start index.html  # Windows
# or
xdg-open index.html  # Linux
```

## 💡 How to Use

### Adding a Task
1. Type your task in the input field
2. Click "Add Task" or press **Enter**
3. Task appears at the top of your list

### Managing Tasks
- **Mark Complete**: Click the checkbox next to a task
- **Delete Task**: Click the "Delete" button on any task
- **Clear Completed**: Click "Clear Completed" to remove all finished tasks

### Filtering Tasks
- **All**: View all tasks
- **Active**: View only incomplete tasks
- **Completed**: View only finished tasks

### Statistics
The app displays:
- **Total**: Total number of tasks
- **Active**: Number of incomplete tasks
- **Completed**: Number of finished tasks

## 🔧 Technical Details

### Local Storage
- Key: `todos_list`
- Format: JSON array of task objects
- Capacity: ~5-10MB per domain

### Task Object Structure
```javascript
{
    id: 1234567890,           // Unique timestamp-based ID
    text: "Task description", // Task text
    completed: false,         // Completion status
    createdAt: "5/2/2026..."  // Creation timestamp
}
```

### JavaScript API

```javascript
// Access the app instance
window.todoApp

// Methods available:
todoApp.addTodo()              // Add new task (from input)
todoApp.deleteTodo(id)         // Delete task by ID
todoApp.toggleTodo(id)         // Toggle completion status
todoApp.clearCompleted()       // Clear all completed tasks
todoApp.getStats()             // Get statistics object
todoApp.exportToJSON()         // Export todos to JSON file
todoApp.importFromJSON(file)   // Import todos from JSON file
todoApp.clearAllData()         // Delete all tasks
```

### Example: Get Statistics
```javascript
const stats = window.todoApp.getStats();
console.log(stats);
// Output:
// {
//   total: 5,
//   completed: 2,
//   active: 3,
//   percentComplete: 40
// }
```

## 🎨 Customization

### Change Color Theme
Edit the color values in `styles.css`:
```css
/* Primary gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Accent colors */
accent-color: #667eea;
background: #ff6b6b;
```

### Change Schedule
Modify the cron time in `.github/workflows/`:
```css
/* Default: 9:00 AM UTC */
/* Change to suit your preferences */
```

### Adjust UI Elements
- Input field placeholder text
- Button labels
- Filter categories
- Statistics display

## 🔒 Data Security

- ✅ **No Server**: All data stored locally in your browser
- ✅ **No Tracking**: No analytics or user tracking
- ✅ **Privacy**: Your tasks stay on your device
- ✅ **Safe**: No external API calls

## ⚠️ Limitations

- Data is **browser-specific** (not synced across devices)
- Data is **per-domain** (clearing browser storage deletes tasks)
- **No backup** automatically created (export manually)
- **5-10MB limit** per domain in most browsers

## 📊 Browser Support

- ✅ Chrome/Edge (88+)
- ✅ Firefox (87+)
- ✅ Safari (14+)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🎯 Future Enhancements

Potential improvements:
- [ ] Cloud sync (Firebase, Supabase)
- [ ] Categories/Tags for tasks
- [ ] Due dates and reminders
- [ ] Recurring tasks
- [ ] Drag-and-drop reordering
- [ ] Dark mode toggle
- [ ] Sound notifications
- [ ] Analytics dashboard

## 📝 Examples

### Example 1: Daily Task List
```
- Review optimization papers
- Update GitHub documentation
- Test constraint solvers
- Prepare presentation
- Email team updates
```

### Example 2: Project Checklist
```
- Design database schema
- Implement API endpoints
- Create UI components
- Write unit tests
- Deploy to production
```

## 🐛 Troubleshooting

### Tasks Not Saving?
- Check if Local Storage is enabled in your browser
- Clear cache and reload
- Try a different browser

### Tasks Lost After Refresh?
- Check browser's Local Storage settings
- Ensure JavaScript is enabled
- Try exporting tasks as backup

### App Not Loading?
- Check browser console for errors (F12)
- Ensure all files are in correct locations
- Try in a different browser

## 💬 Tips & Tricks

1. **Keyboard Shortcuts**
   - Enter to add task
   - Tab to navigate buttons

2. **Bulk Operations**
   - Mark items complete first, then click "Clear Completed"

3. **Backup Your Tasks**
   - Use `exportToJSON()` regularly
   - Save the JSON file in cloud storage

4. **Organization**
   - Use descriptive task names
   - Group related tasks together
   - Use filters to focus on priorities

## 📄 License

MIT License - Feel free to use and modify!

## 🙋 Support

For issues or suggestions:
1. Check the Troubleshooting section
2. Review the Technical Details
3. Check browser console (F12 → Console tab)
4. Create an issue on GitHub

---

**Happy Task Managing!** 🎉

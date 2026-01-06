# 🧪 Development/Test Mode Guide

## Overview

Dev Mode allows you to quickly test the RIASEC questionnaire by auto-filling with random answers without manually answering all 50 questions.

## Quick Start

### Enable Dev Mode

Choose one of these methods:

**Method 1: Click the Button**
- Look for the **🧪 Dev Mode** button in the top-right corner
- Click it to toggle ON (button turns green)

**Method 2: Keyboard Shortcut**
- Press **Shift + D** anywhere on the page
- Dev mode will toggle immediately

### Use Auto-Fill

Once Dev Mode is enabled:

1. Go to **RIASEC Test** tab
2. Click the **🧪 Auto Fill & Submit** button (now visible)
3. All 50 questions are filled with random answers (1-5)
4. Form automatically submits
5. Results appear instantly

**That's it!** ✅ You now have random test results.

---

## Features

### 🎯 What Dev Mode Does

| Feature | Description |
|---------|------------|
| Toggle Button | Easy on/off switch in header |
| Keyboard Shortcut | Shift+D for quick toggling |
| Random Answers | Generates 1-5 scale answers |
| Auto-Submit | Automatically submits the form |
| Instant Results | See results immediately |
| Persistent State | Remembers dev mode setting |

### 🔧 Technical Details

**Random Answer Generation:**
- Each question gets a random value from 1 to 5
- Mimics actual user responses
- Different results each time

**Auto-Submit Flow:**
1. Fill all 50 radio buttons with random values
2. Trigger change events for tracking
3. Dispatch submit event to form
4. Show results automatically

**Persistence:**
- Dev mode state stored in `localStorage`
- Survives page refresh
- Can be disabled anytime

---

## Usage Examples

### Example 1: Quick Test Run
```
1. Open website in browser
2. Press Shift+D (enable dev mode - button turns green)
3. Go to RIASEC Test tab
4. Click "Auto Fill & Submit"
5. Get instant results! ✅
6. Press Shift+D again (disable dev mode - button turns red)
```

### Example 2: Testing Different Results
```
1. Enable Dev Mode
2. Click "Auto Fill & Submit"
3. Get result A
4. Click "Làm lại" (Redo)
5. Click "Auto Fill & Submit"
6. Get different result B (random answers are different)
```

### Example 3: Hide Dev Mode When Done
```
1. Testing complete
2. Press Shift+D to disable dev mode
3. Button returns to hidden state
4. Ready for production/live use
```

---

## Visual Guide

### Dev Mode Button States

**Dev Mode OFF** (Default)
- Button: 🧪 Dev Mode OFF
- Color: Red (#ff6b6b)
- Auto-fill button: Hidden
- Usage: Click to enable

**Dev Mode ON**
- Button: 🧪 Dev Mode ON
- Color: Green (#51cf66)
- Auto-fill button: Visible
- Usage: Ready to auto-fill

### Auto-Fill Button

**When Visible** (Dev Mode ON):
- Text: 🧪 Auto Fill & Submit
- Color: Red
- Click to fill all answers + submit

**When Hidden** (Dev Mode OFF):
- Not visible
- No interaction available

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Shift + D** | Toggle Dev Mode ON/OFF |

---

## Troubleshooting

### Button Not Appearing?
- Make sure you're on the RIASEC Test page
- Enable Dev Mode (button should turn green)
- Refresh if needed

### Auto-Fill Not Working?
- Check browser console (F12) for errors
- Make sure Dev Mode is enabled (green button)
- Clear browser cache and refresh
- Try keyboard shortcut Shift+D first

### Results Not Showing?
- Wait a moment for form submission
- Check if page scrolled to results area
- Try "Làm lại" (Redo) button to reset and try again

---

## For Production

**Important:** Disable or hide dev mode before going live!

**Options:**
1. Simply disable (press Shift+D or click button)
2. Or modify code to require environment variable:
   ```javascript
   // Only show dev mode in development
   if (process.env.NODE_ENV === 'development') {
     showDevMode();
   }
   ```

---

## Code Location

**Dev Mode Implementation:**
- `index.html` - Lines 80-133
- `index1.html` - Lines 191-263

**Key Functions:**
- `fillRandomAnswers()` - Generates random answers
- `updateDevModeUI()` - Updates button state
- Keyboard listener - Handles Shift+D

---

## Benefits

✅ **Save Time** - No need to answer 50 questions manually  
✅ **Fast Testing** - Quick iteration and testing  
✅ **Realistic Results** - Random answers mimic real usage  
✅ **Easy Toggle** - One click or keyboard shortcut  
✅ **No Data Loss** - Dev mode doesn't interfere with real data  

---

## Future Enhancements

Possible improvements:
- [ ] Configurable answer range (not just 1-5)
- [ ] Preset patterns (all 5s, all 1s, etc.)
- [ ] Bulk clear database
- [ ] Export test results
- [ ] Speed up auto-submit animation

---

## Questions?

Check the main documentation:
- `README.md` - Full project documentation
- `QUICKSTART.md` - Setup instructions
- `SETUP_GUIDE.md` - Troubleshooting guide

---

**Last Updated:** 2025-01-06  
**Version:** 1.0  
**Status:** ✅ Production Ready

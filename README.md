# 📞 Phone Call Automation via Microsoft Phone Link
<em>Automated Voice Call Dialing Using Windows UI Automation</em> <br/>
<strong>Note:</strong> This project interacts with Microsoft Phone Link via UI automation — <strong>not</strong> through any official API. It simulates human interaction with the app’s interface to initiate phone calls. Use responsibly and in compliance with local telecommunications regulations.

## ✅ Overview
This Python script automates dialing voice calls to a list of phone numbers using <strong>Microsoft Phone Link</strong> on Windows. It provides <strong>two implementation approaches</strong>:</p>
<table>
<thead>
  <tr>
    <th>Approach</th>
    <th>Method</th>
    <th>Reliability</th>
    <th>Best For</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><strong>1. Hardcoded Coordinates</strong></td>
    <td>Uses fixed screen positions (<code>pyautogui.click(x, y)</code>)</td>
    <td>⚠️ Low — breaks with screen scaling/UI changes</td>
    <td>Quick testing, single-device use</td>
  </tr>
  <tr>
    <td><strong>2. Screenshot-Based</strong></td>
    <td>Uses image recognition (<code>pyautogui.locateOnScreen()</code>)</td>
    <td>✅ High — works across resolutions and minor UI changes</td>
    <td>Production use, portability, reliability</td>
  </tr>
</tbody>
</table>

Both approaches read phone numbers from <code>phone_numbers.csv</code>, initiate calls via Phone Link, and log results to <code>logs/dial_log.txt</code>.

## 🛠️ Prerequisites
### ✅ Software Requirements
<ul>
  <li><strong>Windows 10/11</strong> (Phone Link requires Windows)</li>
  <li><strong>Microsoft Phone Link</strong> installed and connected to your Android device</li>
  <li><strong>Python 3.8+</strong></li>
</ul>

### 📦 Python Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```


## 📁 Project Structure
<pre>
Phone-Call-Automation/
│
├── dial_coordinates.py           # Coordinate-based approach
├── dial_screenshots.py           # Screenshot-based approach
├── contacts.csv             # CSV file with phone numbers (one per row)
├── logs/                         # Auto-generated log file (dial_log.txt)
├── screenshots/             # Folder for UI element images (Screenshot approach only)
│   ├── phone_tab.png
│   ├── dial_button.png
│   ├── call_button.png
│   └── hangup_button.png
│
└── README.md                 
</pre>

<p><strong>✅ Create the folders <code>logs/</code> and <code>screenshots/</code> before running the script.</strong></p>

<h2>📄 File Formats</h2>

<h3>1. <code>contacts.csv</code></h3>
<p>Format: One phone number per row.<br>
<strong>Example:</strong></p>
<pre>
0704581833
0712345678
0798765432
</pre>

<strong>❗ Ensure numbers are <em>numeric only</em></strong> (no spaces, +, or dashes). The script will skip invalid entries and log them.

### 2. Screenshots (Screenshot Approach Only)
Take <strong>clear, high-contrast screenshots</strong> of these elements in Microsoft Phone Link:

<table>
  <thead>
    <tr>
      <th>Element</th>
      <th>Screenshot Name</th>
      <th>How to Capture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Phone Tab</td>
      <td><code>phone_tab.png</code></td>
      <td>Click the "Phone" tab in Phone Link sidebar</td>
    </tr>
    <tr>
      <td>Dial Pad Button</td>
      <td><code>dial_button.png</code></td>
      <td>The dial pad/keyboard icon that opens number input</td>
    </tr>
    <tr>
      <td>Call Button</td>
      <td><code>call_button.png</code></td>
      <td>The green call button (usually circular)</td>
    </tr>
    <tr>
      <td>Hangup Button</td>
      <td><code>hangup_button.png</code></td>
      <td>The red hangup button (for auto-hangup)</td>
    </tr>
  </tbody>
</table>

<strong>🔍 Tips for better recognition:</strong>
<ul>
  <li>Use <strong>100% zoom</strong> in Phone Link</li>
  <li>Avoid shadows, transparency, or blurred edges</li>
  <li>Save as <strong>PNG</strong> (not JPG)</li>
  <li>Match the <strong>exact name</strong> in the code</li>
</ul>

<strong>💡 You can use Windows Snipping Tool or Snip & Sketch to capture these.</strong>

## ▶️ Setup & Run Instructions
### ✅ Step 1: Prepare Your Environment
<ol>
  <li>Create the folders:
    <pre>mkdir logs screenshots</pre>
  </li>
  <li>Place your phone numbers in <code>contacts.csv</code></li>
  <li>(For Screenshot Approach) Add your screenshot files into the <code>screenshots/</code> folder</li>
</ol>

### ✅ Step 2: Choose Your Approach
####🔧 Approach 1: Hardcoded Coordinates
Use this if you just want to test quickly on your current screen setup.
<ol>
  <li>Open <code>dial_coordinates.py</code> and <strong>update the coordinates</strong> to match your Phone Link UI:
    <ul>
      <li>Phone tab coordinates</li>
      <li>Dial button coordinates</li>
      <li>Call button coordinates</li>
    </ul>
  </li>
  <li>Run the script:
    <pre>python dial_coordinates.py</pre>
  </li>
</ol>

#### 🖼️ Approach 2: Screenshot-Based (Recommended)
Use this for reliability across devices and future-proofing.
<ol>
  <li>Ensure your <code>screenshots/</code> folder contains:
    <ul>
      <li><code>phone_tab.png</code></li>
      <li><code>dial_button.png</code></li>
      <li><code>call_button.png</code></li>
      <li><code>hangup_button.png</code></li>
    </ul>
  </li>
  <li>Run the script:
    <pre>python dial_screenshots.py</pre>
  </li>
</ol>

## ⚙️ How It Works
### Main Workflow:
<ol>
  <li>Script reads <code>contacts.csv</code></li>
  <li>Waits 5 seconds for you to open and focus <strong>Microsoft Phone Link</strong></li>
  <li>For each number:
    <ul>
      <li>Clicks the Phone tab (if needed)</li>
      <li>Opens the dial pad</li>
      <li>Types the phone number → clicks call button</li>
      <li>Logs result to <code>logs/dial_log.txt</code></li>
    </ul>
  </li>
</ol>

### Logging
All dialing attempts are recorded in <code>logs/dial_log.txt</code>:
<pre>
[2025-11-22 15:30:25] SUCCESS - 0704581833
[2025-11-22 15:31:10] FAILED - 0712345678 (Could not find dial_pad_button after 10 seconds)
[2025-11-22 15:32:05] FAILED - 123abc (Invalid number)
</pre>

## 🚨 Important Notes & Limitations
<table>
  <thead>
    <tr>
      <th>Consideration</th>
      <th>Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>No API</strong></td>
      <td>This uses UI automation — not a supported or secure method. Use for personal automation only.</td>
    </tr>
    <tr>
      <td><strong>Phone Link Must Be Active</strong></td>
      <td>The Phone Link window must be <strong>visible, focused, and unlocked</strong> on your desktop.</td>
    </tr>
    <tr>
      <td><strong>Screen Resolution Matters</strong></td>
      <td>Hardcoded coordinates break if you change resolution or scale. Screenshot approach is resilient.</td>
    </tr>
    <tr>
      <td><strong>Call Duration</strong></td>
      <td>By default, calls remain active until manually hung up. Auto-hangup is optional.</td>
    </tr>
    <tr>
      <td><strong>Android Sync Required</strong></td>
      <td>Your phone must be connected to Phone Link and call functionality enabled.</td>
    </tr>
    <tr>
      <td><strong>Ethics & Compliance</strong></td>
      <td>Do not make unsolicited calls. Respect privacy and local telecommunications laws.</td>
    </tr>
    <tr>
      <td><strong>Network Dependency</strong></td>
      <td>Your phone must have cellular service for calls to connect.</td>
    </tr>
  </tbody>
</table>

## 🛠️ Troubleshooting
<table>
  <thead>
    <tr>
      <th>Issue</th>
      <th>Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Could not find [element] after 10 seconds</code></td>
      <td>Take a new screenshot of the missing UI element. Ensure it’s in <code>screenshots/</code> with correct name.</td>
    </tr>
    <tr>
      <td>Script clicks wrong location (coordinates)</td>
      <td>Recalibrate coordinates using a mouse position finder script.</td>
    </tr>
    <tr>
      <td>Phone Link doesn’t respond</td>
      <td>Restart Phone Link and reconnect your phone. Run script as Administrator if needed.</td>
    </tr>
    <tr>
      <td><code>Image not found</code> error</td>
      <td>Check spelling of screenshot filenames. They must match exactly.</td>
    </tr>
    <tr>
      <td><code>The confidence keyword argument is only available if OpenCV is installed</code></td>
      <td>Install OpenCV: <code>pip install opencv-python</code></td>
    </tr>
    <tr>
      <td>Numbers not dialing correctly</td>
      <td>Ensure numbers are numeric only (no +, spaces, or dashes)</td>
    </tr>
  </tbody>
</table>

  #### 💡 Pro Tips:
  <ul>
    <li>✅ Test first: Run with <strong>one number</strong> before bulk dialing.</li>
    <li>✅ Use <strong>Screenshot Approach</strong> for any serious or repeated use.</li>
    <li>✅ Run in full-screen mode on a 1920x1080 or higher display for best results.</li>
    <li>✅ Always check logs — they tell you exactly what failed and why.</li>
    <li>✅ Backup your screenshots — if you update Windows or Phone Link, re-capture them.</li>
    <li>✅ Consider auto-hangup for testing to avoid tying up your phone line.</li>
  </ul>

## 📌 Final Notes
This project demonstrates advanced <strong>UI automation techniques</strong> for applications without APIs — a valuable skill in systems integration, accessibility tools, and legacy software automation. <br/>
<em>While not ideal for enterprise telecommunications, this solution proves that with creativity and persistence, even closed interfaces can be automated — ethically and effectively for personal productivity.</em>

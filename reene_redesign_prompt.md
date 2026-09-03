# REENE Medical Diagnostics Website - Professional Redesign Prompt

## CRITICAL: Make it Look Less AI-Generated & More Professional

### 1. DESIGN SYSTEM OVERHAUL

**Typography:**
- Headlines: Use **60-72px** for H1 (bold, 700 weight) with **1.1 line-height** max
- Subheadings: **32-40px** H2 with careful line spacing
- Body text: **16-18px** with **1.6 line-height** (NOT cramped)
- Small text: **14px** max only for captions
- Font family: Use system fonts or load Google Fonts properly (Poppins + Inter)

**Spacing & Rhythm:**
- Base unit: **8px grid system**
- Section margins: **60-80px vertical** (not uniform everywhere)
- Card padding: **32px** (not 24px)
- Paragraph margins: **24px** between text blocks
- Inconsistent spacing = feels intentional, not templated

**Color Palette - Use Strategically:**
- Primary Blue: #003D7A (not bright) - use for CTAs only
- Accent: #FF4B4B (red) - for important elements only
- Background: #F8F9FB (subtle gray, not white)
- Dark text: #1A202C (not pure black)
- Don't fill every element with color - lots of white space

**Icons - Use Lucide React (NOT Emoji):**
- Library: `lucide-react` 
- Icon size: **64px for services, 56px for features, 32px for nav**
- Stroke width: **1.5** (professional thin stroke)
- Color: **#003D7A** (primary blue)
- Background circles: **#EFF6FF** (light blue, 56px size for service icons)

**Common Medical Icons from Lucide:**
- Laboratory: `Microscope`, `TestTube`, `Pipette`
- Ultrasound: `Waves`, `Radio`, `Activity`
- Imaging: `Zap`, `Scan`, `Eye`
- Cardiac: `Heart`, `Pulse`, `Activity`
- General: `Building2`, `Users`, `Calendar`, `MapPin`, `Phone`

**Icon Usage Example:**
```jsx
import { Microscope } from 'lucide-react';

<div className="bg-blue-50 rounded-full p-4 w-fit">
  <Microscope size={64} strokeWidth={1.5} className="text-blue-600" />
</div>
```

---

### 2. HERO SECTION IMPROVEMENTS

**Current Problem:** Looks generic
**Solution:**
- Hero image on right should have **subtle shadow & rounded corners (12px)**
- Text should be **dark navy** (#003D7A), not light on dark
- Add a small **"NOW ACCEPTING WALK-INS"** badge above heading
- Heading should span **2-3 lines naturally** (not all on one line)
- Remove centered text layout - use **left-aligned** text with **asymmetric image placement**

---

### 3. CONTENT CARD IMPROVEMENTS

**Make Cards Look Professional:**
- Add **1px solid #E2E8F0** borders instead of shadows only
- Use **12px rounded corners**
- Padding inside cards: **28px** (not 20px)
- When hovering, card should move up **4px** smoothly (not scale)
- Icon should be **56x56px** with subtle background circle (#EFF6FF)
- Title: **20px bold**, Description: **14px medium** with **1.5 line-height**

**Gallery Grid:**
- Use **masonry layout** (not uniform grid)
- Alternate image sizes: some **tall**, some **wide**, some **square**
- Add **soft overlay on hover** (0.1 opacity black)
- Images should have **8px gaps** between them, not 16px

---

### 4. NAVIGATION & HEADER

**Header should be:**
- Fixed/sticky with **subtle shadow** only on scroll
- Logo: **32x32px** (not oversized)
- Nav links: **14px medium weight**, spaced **24px** apart
- Active link: **underline only** (not background color)
- CTA button: **rounded 8px**, **14px text**, **44px height**
- Mobile: Hamburger menu with **slide-in sidebar** from right

---

### 5. FORMS - MAKE THEM LOOK REAL

**Form Inputs:**
- Border: **2px #E2E8F0** (not 1px)
- Padding: **12px 16px**
- Rounded: **8px**
- Focus state: **2px solid #003D7A** border + shadow
- Label: **14px medium**, **12px above** input
- Placeholder: **#A0AEC0** (medium gray, visible)
- Focus placeholder: becomes invisible
- Error: **#EF4444** text below field

**Submit Button:**
- **44px height minimum**
- **16px padding horizontal**
- Hover: **background darkens** by 10% (not scale)
- Active: **2px inset shadow**
- Loading: **spinner animation**

---

### 6. TESTIMONIALS & SOCIAL PROOF

**Make It Feel Real (Not AI):**
- Use **actual quotes** with **quotation mark icon**
- Include **date posted** ("2 weeks ago")
- Avatar: **48x48px circle**, **4px border**
- Rating stars: **show real count** ("4.8/5 from 127 reviews")
- Add **"Verified Patient"** badge
- Testimonial cards: **left border accent** (4px colored)

---

### 7. CTA SECTIONS - MAKE THEM CLICK

**"Book Appointment" Areas:**
- Should appear **3 times minimum** (top, middle, bottom)
- Button text variations: "Book Appointment", "Schedule Now", "Call Us"
- Pair button with **phone icon** OR **calendar icon** for context
- Add urgency: **"Same-day appointments available"** in small text

---

### 8. FOOTER - ORGANIZE BETTER

**Footer should have:**
- **4 columns max** on desktop
- Column headers: **14px bold** (#003D7A)
- Links: **14px medium**, **8px spacing** between
- Social icons: **32x32px**, **circular**, proper padding
- Bottom bar: **copyright + links (Privacy, Terms)**
- Background: **#0F1729** (dark, not pure black)

---

### 9. ABOUT US PAGE SPECIFICS

**Match Reference Image:**
- **Wide hero image** (facility photo) at top
- Text overlay: **"About Reene Medical Diagnostics"** left-aligned
- Stats section: **4 columns** (25+, 50+, 10000+, 98%)
  - Stat number: **48px bold** (#003D7A)
  - Stat label: **14px medium**
  - Background: **subtle box** (#EFF6FF)
- Mission/Vision: **2 column layout** with **left border accent**
- Team section: **3-4 person cards** with **real photo** + role

---

### 10. SERVICES PAGE SPECIFICS

**Service Cards Layout:**
- **6 service cards** in 3x2 grid or masonry
- Each card: **360px width**, **rounded 12px border**
- Image: **280px height**, **rounded top 12px**
- Badge: **positioned top-right**, **40px circular**
- Title: **18px bold**
- Description: **14px**, **2-3 lines max**
- "Learn More →" link: **blue text** with **underline on hover**

**Service Details Sections:**
- Section title: **36px bold**, centered
- Icons: **Lucide React 64px** (stroke-width 1.5), **NOT emoji**
  - Laboratory Tests: `Microscope`
  - Ultrasound: `Waves` 
  - CT Scan: `Zap`
  - MRI: `Radio`
  - X-Ray: `Zap`
  - ECG: `Heart`
  - Icon color: **#003D7A** (blue)
  - Icon background: **circular #EFF6FF** (light blue circle, 56px)
- Description: **16px**, **max 80 character width**

---

### 11. CONTACT PAGE IMPROVEMENTS

**Map Section:**
- **Full-width** on desktop, **responsive** on mobile
- Rounded corners: **12px**
- Overlay info box with **background blur** or **semi-transparent white**

**Contact Form:**
- **2 column layout** on desktop (left form, right info)
- Form width: **max 500px**
- All fields: **single column** (not cramped)
- Required star: **red** (#EF4444)
- Success message: **success toast** (not alert)

**Contact Info Cards:**
- Icons: **blue circular background** (#EFF6FF)
- Info text: **16px black**, subtext **14px gray**
- Spacing: **24px between cards**

---

### 12. MICRO-INTERACTIONS & ANIMATIONS

**Remove Clunky AI Feel With:**
- Smooth transitions: **all 0.3s ease-in-out**
- Buttons: **hover state** changes background, no scale
- Links: **underline on hover**, color shift
- Icons: **rotate/move slightly on hover** (subtle)
- Page transitions: **fade in 0.4s** from top
- Scroll animations: elements fade in as you scroll (not bounce)

---

### 13. MOBILE OPTIMIZATION

- **Touch targets**: minimum **48px height**
- **Font sizes**: bump to **18px** for body text
- **Spacing**: increase margins by **1.5x**
- **Images**: full-width with **aspect-ratio** maintained
- **Forms**: single column, larger inputs
- **Navigation**: mobile menu slides in smoothly
- Test on **iPhone 12 & Android devices**

---

### 14. COPY & MESSAGING - Remove Generic AI Feel

**Replace Generic Copy With Specific Details:**

❌ "Comprehensive diagnostics with advanced technology"
✅ "Certified ultrasonographers using Siemens S3000 equipment deliver results in 24-48 hours"

❌ "Patient-centered care"
✅ "Compassionate care with same-day reports & WhatsApp follow-up"

❌ "Trusted partner"
✅ "Trusted by 10,000+ patients across Anambra since 2008"

- Add **specific numbers** (50+ services, 6 expert physicians)
- Use **location names** (Awada, Onitsha LGA)
- Include **real features** (licensed, certified, accredited)

---

### 15. IMAGE OPTIMIZATION

**Photo Strategy:**
- Use **high-quality facility photos** (not stock images)
- Include **real staff photos** (professional headshots)
- Equipment photos: **clean, well-lit**
- Patient photos: use **diverse representation**
- All images: **optimized for web** (compress, lazy load)
- Image alt text: descriptive

---

### 16. BEFORE/AFTER - Visual Checklist

**Generic AI Look → Professional Medical Site:**

- [ ] Remove drop shadows everywhere, use subtle borders
- [ ] Fix text sizing (headlines too big relative to body)
- [ ] Tighten line-height for readability
- [ ] Add white space between sections (not cramped)
- [ ] Use color strategically (not every element colored)
- [ ] Fix card padding (increase from 20→28px)
- [ ] Replace placeholder icons with professional SVGs
- [ ] Add real testimonials with dates/verification
- [ ] Improve form labels and input styling
- [ ] Make buttons look clickable (shadow on hover)
- [ ] Add actual numbers/stats (not "50+ Services")
- [ ] Improve typography hierarchy
- [ ] Add smooth page transitions
- [ ] Optimize for mobile first
- [ ] Replace generic copy with specific details

---

### 17. FINAL POLISH

**Quality Checks:**
1. **Accessibility**: All buttons 44px+ height, color contrast ≥4.5:1
2. **Performance**: Lighthouse score >85
3. **Consistency**: Same heading styles throughout
4. **Responsiveness**: Test on 6 different screen sizes
5. **Browser Compatibility**: Chrome, Firefox, Safari, Edge
6. **Load Times**: All images compressed, lazy loaded
7. **SEO**: Meta descriptions, structured data, alt text

---

## Summary for Claude Code

Focus on these 3 things to remove "AI-generated" feel:

1. **Specificity** - Real numbers, real copy, real photos (not generic placeholders)
2. **Restraint** - Lots of white space, selective color use, subtle interactions
3. **Professional Polish** - Proper spacing, typography hierarchy, smooth animations

The difference between "looks AI-made" and "looks professional" is often just better spacing, real content, and strategic simplicity.

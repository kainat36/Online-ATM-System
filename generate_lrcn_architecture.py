"""
LRCN Architecture Diagram Generator
Generates a detailed architecture diagram for the Long-Term Recurrent Convolutional Network
used for fall detection based on the research paper description.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Color scheme
color_input = '#E8F4F8'
color_conv = '#4A90E2'
color_pool = '#7ED321'
color_dropout = '#F5A623'
color_flatten = '#BD10E0'
color_lstm = '#D0021B'
color_dense = '#50E3C2'
color_output = '#B8E986'

# Helper function to draw a layer box
def draw_layer(ax, x, y, width, height, color, label, details='', fontsize=10):
    """Draw a layer box with label and details"""
    box = FancyBboxPatch((x, y), width, height, 
                          boxstyle="round,pad=0.05", 
                          edgecolor='black', 
                          facecolor=color, 
                          linewidth=2,
                          zorder=2)
    ax.add_patch(box)
    
    # Add label
    ax.text(x + width/2, y + height/2 + 0.15, label, 
            ha='center', va='center', fontsize=fontsize, 
            fontweight='bold', zorder=3)
    
    # Add details
    if details:
        ax.text(x + width/2, y + height/2 - 0.15, details, 
                ha='center', va='center', fontsize=fontsize-2, 
                style='italic', zorder=3)

# Helper function to draw arrows
def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Draw an arrow between layers"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', 
                           mutation_scale=30, 
                           linewidth=2.5,
                           color='#333333',
                           zorder=1)
    ax.add_patch(arrow)
    
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.3, mid_y, label, 
                ha='center', va='center', 
                fontsize=8, 
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray'),
                zorder=3)

# Title
ax.text(5, 13.5, 'LRCN Architecture for Fall Detection', 
        ha='center', va='top', fontsize=18, fontweight='bold')
ax.text(5, 13, 'Long-Term Recurrent Convolutional Network', 
        ha='center', va='top', fontsize=12, style='italic', color='gray')

# Layer positions
y_start = 11.5
layer_height = 0.6
layer_width = 1.8
x_center = 5

# Input Layer
draw_layer(ax, x_center - layer_width/2, y_start, layer_width, layer_height, 
           color_input, 'Input Sequence', '23 frames\n64×64×3', fontsize=10)
y_current = y_start

# Arrow down
draw_arrow(ax, x_center, y_current, x_center, y_current - 0.5)
y_current -= 0.5

# TimeDistributed wrapper label
ax.text(0.5, y_current - 2.5, 'TimeDistributed\nWrapper', 
        ha='center', va='center', fontsize=10, 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0F0F0', edgecolor='black', linewidth=2),
        rotation=0)

# Block 1: Conv2D + MaxPool + Dropout
y_current -= 0.7
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_conv, 'Conv2D (1)', 'Filters: 16\nKernel: 3×3\nActivation: ReLU', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_pool, 'MaxPooling2D', 'Pool: 2×2', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_dropout, 'Dropout', 'Rate: 0.3', fontsize=9)

# Block 2: Conv2D + MaxPool + Dropout
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_conv, 'Conv2D (2)', 'Filters: 32\nKernel: 3×3\nActivation: ReLU', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_pool, 'MaxPooling2D', 'Pool: 2×2', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_dropout, 'Dropout', 'Rate: 0.4', fontsize=9)

# Block 3: Conv2D + MaxPool + Dropout
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_conv, 'Conv2D (3)', 'Filters: 64\nKernel: 3×3\nActivation: ReLU', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_pool, 'MaxPooling2D', 'Pool: 2×2', fontsize=9)

y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_dropout, 'Dropout', 'Rate: 0.5', fontsize=9)

# Block 4: Conv2D (consolidation)
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_conv, 'Conv2D (4)', 'Filters: 64\nKernel: 3×3\nActivation: ReLU', fontsize=9)

# Flatten Layer
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_flatten, 'Flatten', 'Per-frame features', fontsize=9)

# LSTM Layer
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1, 'Temporal\nSequence')
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_lstm, 'LSTM', 'Units: 32\nTemporal modeling', fontsize=9)

# Dense Layer (Softmax)
y_current -= 0.8
draw_arrow(ax, x_center, y_current + 0.8, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_dense, 'Dense (Softmax)', '2 classes', fontsize=9)

# Output Layer
y_current -= 0.7
draw_arrow(ax, x_center, y_current + 0.7, x_center, y_current + 0.1)
draw_layer(ax, x_center - layer_width/2, y_current, layer_width, layer_height, 
           color_output, 'Output', 'Fall / Not-Fall\nProbabilities', fontsize=9)

# Add information boxes on the sides
# Left side - Training Configuration
info_box_left = """Training Configuration:
• Optimizer: Adam
• Loss: Categorical Cross-Entropy
• Batch Size: 4
• Early Stopping: Patience 10
• Regularization: Dropout (0.3-0.5)"""

ax.text(0.3, 8, info_box_left, 
        ha='left', va='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF9E6', 
                  edgecolor='#FFB84D', linewidth=2))

# Right side - Evaluation Metrics
info_box_right = """Evaluation Metrics:
• Precision
• Recall
• Accuracy

Architecture Type:
• LRCN (Long-Term Recurrent
  Convolutional Network)
• Spatial: Conv2D layers
• Temporal: LSTM layer"""

ax.text(9.7, 8, info_box_right, 
        ha='right', va='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.8', facecolor='#E6F7FF', 
                  edgecolor='#4A90E2', linewidth=2))

# Add legend
legend_elements = [
    mpatches.Patch(facecolor=color_input, edgecolor='black', label='Input'),
    mpatches.Patch(facecolor=color_conv, edgecolor='black', label='Convolutional'),
    mpatches.Patch(facecolor=color_pool, edgecolor='black', label='Pooling'),
    mpatches.Patch(facecolor=color_dropout, edgecolor='black', label='Dropout'),
    mpatches.Patch(facecolor=color_flatten, edgecolor='black', label='Flatten'),
    mpatches.Patch(facecolor=color_lstm, edgecolor='black', label='LSTM'),
    mpatches.Patch(facecolor=color_dense, edgecolor='black', label='Dense'),
    mpatches.Patch(facecolor=color_output, edgecolor='black', label='Output')
]

ax.legend(handles=legend_elements, loc='lower center', 
          bbox_to_anchor=(0.5, -0.05), ncol=8, fontsize=9,
          frameon=True, fancybox=True, shadow=True)

# Add footer
ax.text(5, 0.3, 'LRCN integrates convolutional layers for spatial representation with recurrent layers for temporal dynamics', 
        ha='center', va='bottom', fontsize=9, style='italic', color='gray')

# Adjust layout and save
plt.tight_layout()
plt.savefig('/vercel/sandbox/LRCN_Architecture_Diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Architecture diagram saved as: LRCN_Architecture_Diagram.png")
print("✓ Resolution: 300 DPI")
print("✓ Format: PNG")

# Also save as PDF for publication quality
plt.savefig('/vercel/sandbox/LRCN_Architecture_Diagram.pdf', bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ PDF version saved as: LRCN_Architecture_Diagram.pdf")

plt.show()

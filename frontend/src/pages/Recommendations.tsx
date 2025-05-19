import React from 'react';
import {
  Box,
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Chip,
} from '@mui/material';
import BookmarkIcon from '@mui/icons-material/Bookmark';

const Recommendations: React.FC = () => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h4" gutterBottom>
        Recommended Papers
      </Typography>
      
      <Typography variant="body1" sx={{ mb: 3 }}>
        Based on your reading history and interests, we think you might like these papers:
      </Typography>

      <Grid container spacing={3}>
        {/* Example recommendation card - will be populated dynamically */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Example Paper Title
              </Typography>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                Authors: John Doe, Jane Smith
              </Typography>
              <Box sx={{ mt: 1, mb: 2 }}>
                <Chip label="Machine Learning" sx={{ mr: 1 }} />
                <Chip label="Neural Networks" />
              </Box>
              <Typography variant="body2">
                This is a brief abstract or summary of the recommended paper...
              </Typography>
            </CardContent>
            <CardActions>
              <Button
                size="small"
                startIcon={<BookmarkIcon />}
              >
                Save for Later
              </Button>
              <Button size="small" color="primary">
                View Details
              </Button>
            </CardActions>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Recommendations; 
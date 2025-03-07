
package com.example.voiceassistantapp

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import androidx.activity.compose.ManagedActivityResultLauncher
import androidx.activity.result.ActivityResultLauncher
import java.util.Locale
import com.example.voiceassistantapp.ui.theme.VoiceAssistantAppTheme



val appPackageMap = mapOf(
    "whatsapp" to "com.whatsapp",
    "browser" to "com.android.chrome",
    "settings" to "com.android.settings",
    "camera" to "com.oplus.camera",
    "YouTube" to "com.google.android.youtube",
    "gmail" to "com.google.android.gm",
    "maps" to "com.google.android.apps.maps",
    "brave" to "com.brave.browser"
)


class MainActivity : ComponentActivity() {
    private fun isAppInstalled(packageName: String, context: android.content.Context): Boolean {
        return try {
            context.packageManager.getPackageInfo(packageName, 0)
            true
        } catch (e: android.content.pm.PackageManager.NameNotFoundException) {
            false
        }
    }
    private var recognizedText by mutableStateOf("press the button and speak")
    private val speechRecognizerLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == RESULT_OK) {
            val data: Intent? = result.data
            val recognizedText = data?.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)?.get(0)
            if (recognizedText != null) {
                this.recognizedText = "You said: $recognizedText"
                // Extract the app name from the recognized text
                val appName = extractAppName(recognizedText)
                if (appName != null) {
                    // Switch to the app
                    switchToApp(appName, this)
                } else {
                    android.widget.Toast.makeText(this, "App not found!", android.widget.Toast.LENGTH_SHORT).show()
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            VoiceAssistantAppTheme {
                VoiceAssistantApp(speechRecognizerLauncher)
            }
        }
    }

}

@Composable
fun VoiceAssistantApp(speechRecognizerLauncher: androidx.activity.result.ActivityResultLauncher<Intent>) {
    val context = LocalContext.current
    var recognizedText by remember { mutableStateOf("Press the button and speak") }

    LaunchedEffect(recognizedText) {
        if (recognizedText.isNotEmpty()) {
            android.widget.Toast.makeText(context, "Welcome user", android.widget.Toast.LENGTH_SHORT).show()
        }
    }
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(
            text = recognizedText,
            fontSize = 18.sp,
            modifier = Modifier.padding(bottom = 20.dp)
        )

        Button(onClick = {
            startVoiceInput ( context, speechRecognizerLauncher)
        }) {
            Text(text = "Speak")
        }
    }
}

private fun startVoiceInput(context: android.content.Context, launcher: androidx.activity.result.ActivityResultLauncher<Intent>) {
    val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH).apply {
        putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM) // Fixed typo
        putExtra(RecognizerIntent.EXTRA_LANGUAGE, Locale.getDefault())
        putExtra(RecognizerIntent.EXTRA_PROMPT, "Speak something...") // Fixed typo in "Speak"
    }

    if (intent.resolveActivity(context.packageManager) != null) {
        launcher.launch(intent)
    } else {
        android.widget.Toast.makeText(context, "Speech recognition is not supported on this device!", android.widget.Toast.LENGTH_SHORT).show()
    }
}

//private const val REQUEST_CODE_SPEECH_INPUT = 1

// Handle the result of the speech input
@Composable
fun HandleActivityResult(data: Intent?, onResult: (String) -> Unit) {
    if (data != null) {
        val result = data.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)
        if (!result.isNullOrEmpty()) {
            val recognizedText = result[0]
            onResult(recognizedText)

            // Extract the app name from the recognized text
            val appName = extractAppName(recognizedText)
            if (appName != null) {
                // Log the app
                println("Extracted app name : $appName")
                // switch to the app
                switchToApp(appName, LocalContext.current)
            } else {
                android.widget.Toast.makeText(LocalContext.current, "App not found", android.widget.Toast.LENGTH_SHORT).show()
            }


        }
    }
}

// extract the app name from the recognized text

private fun extractAppName(recognizedText: String): String? {
    for ((key, _) in appPackageMap) {
        if (recognizedText.contains(key, ignoreCase = true)) {
            return key
        }
    }
    return null
}

// switch to the app

private fun switchToApp(appName: String, context: android.content.Context) {
    if (appName.equals("youtube", ignoreCase = true)) {
        // Use an implicit intent to open YouTube
        val intent = Intent(Intent.ACTION_VIEW, android.net.Uri.parse("https://www.youtube.com"))
        if (intent.resolveActivity(context.packageManager) != null) {
            context.startActivity(intent)
        } else {
            android.widget.Toast.makeText(context, "YouTube app not found!", android.widget.Toast.LENGTH_SHORT).show()
        }
    } else {
        val packageName = appPackageMap[appName]
        if (packageName != null) {
            val intent = context.packageManager.getLaunchIntentForPackage(packageName)
            if (intent != null) {
                context.startActivity(intent)
            } else {
                android.widget.Toast.makeText(context, "App not installed!", android.widget.Toast.LENGTH_SHORT).show()
            }
        } else {
            android.widget.Toast.makeText(context, "App not found in the map!", android.widget.Toast.LENGTH_SHORT).show()
        }
    }
}
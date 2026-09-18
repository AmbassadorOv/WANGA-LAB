package com.imperialaudit.mobile

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import org.json.JSONObject
import java.security.MessageDigest
import java.time.Instant

private fun canonicalJson(o: JSONObject): String {
    val keys = o.keys().asSequence().toList().sorted()
    val out = JSONObject()
    for (k in keys) out.put(k, o.get(k))
    return out.toString().replace(": ", ":").replace(", ", ",")
}
private fun sha256(s: String): String =
    MessageDigest.getInstance("SHA-256").digest(s.toByteArray(Charsets.UTF_8))
        .joinToString("") { "%02x".format(it) }

private fun buildChain(a: JSONObject, b: JSONObject, c: JSONObject, timestamp: String): JSONObject {
    val h1=sha256(canonicalJson(a)); val h2=sha256(canonicalJson(b)); val h3=sha256(canonicalJson(c))
    val master=sha256("S1=$h1\nS2=$h2\nS3=$h3\nTIMESTAMP=$timestamp")
    return JSONObject().apply { put("S1",h1); put("S2",h2); put("S3",h3); put("MASTER_CHAIN_HASH",master) }
}

@Composable fun Field(label:String,value:String,onValue:(String)->Unit){
    OutlinedTextField(value,onValue,label={Text(label)},modifier=Modifier.fillMaxWidth().padding(vertical=4.dp),minLines=3)
}

@Composable fun App(){
    var tab by remember{mutableStateOf(0)}
    var a by remember{mutableStateOf("{\"exposure\":0}")}
    var b by remember{mutableStateOf("{\"parameters\":{}}")}
    var c by remember{mutableStateOf("{\"recovery\":{}}")}
    var output by remember{mutableStateOf("")}
    var input by remember{mutableStateOf("")}
    var status by remember{mutableStateOf("")}

    MaterialTheme{
        Scaffold(topBar={TopAppBar(title={Text("Imperial Audit")})}){pad->
            Column(Modifier.padding(pad).padding(16.dp).verticalScroll(rememberScrollState())){
                Row(horizontalArrangement=Arrangement.spacedBy(8.dp)){
                    Button(onClick={tab=0}){Text("יצירה")}
                    Button(onClick={tab=1}){Text("אימות")}
                }
                Spacer(Modifier.height(12.dp))
                if(tab==0){
                    Text("Offline Evidence Builder",style=MaterialTheme.typography.headlineSmall)
                    Text("הכלי בונה חבילת נתונים מקומית ומחשב שרשרת SHA-256. הוא אינו קובע לבדו אמיתות נתונים או תוקף משפטי.")
                    Field("S1",a){a=it}; Field("S2",b){b=it}; Field("S3",c){c=it}
                    Button(onClick={
                        try{
                            val t=Instant.now().toString()
                            val chain=buildChain(JSONObject(a),JSONObject(b),JSONObject(c),t)
                            output=JSONObject().apply{
                                put("schema_version","8.0")
                                put("system_identifier","imperial-audit-core")
                                put("timestamp_utc",t)
                                put("S1",JSONObject(a)); put("S2",JSONObject(b)); put("S3",JSONObject(c))
                                put("cryptographic_integrity",chain)
                                put("external_proofs",JSONObject().apply{
                                    put("rfc3161","PENDING_EXTERNAL_TSA")
                                    put("opentimestamps","PENDING_EXTERNAL_ANCHOR")
                                })
                                put("legal_status","TECHNICAL_EVIDENCE_ONLY_REQUIRES_LEGAL_REVIEW")
                            }.toString(2)
                        }catch(e:Exception){output="ERROR: "+e.message}
                    },modifier=Modifier.fillMaxWidth()){Text("צור Evidence Package")}
                    if(output.isNotBlank()){Spacer(Modifier.height(8.dp));Text(output,style=MaterialTheme.typography.bodySmall)}
                }else{
                    Text("Evidence Verification",style=MaterialTheme.typography.headlineSmall)
                    Field("JSON",input){input=it}
                    Button(onClick={
                        try{
                            val p=JSONObject(input); val t=p.getString("timestamp_utc")
                            val expected=buildChain(p.getJSONObject("S1"),p.getJSONObject("S2"),p.getJSONObject("S3"),t)
                            val actual=p.getJSONObject("cryptographic_integrity")
                            status=if(expected.getString("MASTER_CHAIN_HASH")==actual.getString("MASTER_CHAIN_HASH") &&
                                expected.getString("S1")==actual.getString("S1") &&
                                expected.getString("S2")==actual.getString("S2") &&
                                expected.getString("S3")==actual.getString("S3")) "VERIFIED — השרשרת תואמת" else "FAILED — אי-התאמה"
                        }catch(e:Exception){status="INVALID PACKAGE — "+e.message}
                    },modifier=Modifier.fillMaxWidth()){Text("אמת שרשרת")}
                    Spacer(Modifier.height(8.dp));Text(status)
                }
            }
        }
    }
}
class MainActivity:ComponentActivity(){
    override fun onCreate(savedInstanceState:Bundle?){super.onCreate(savedInstanceState);setContent{App()}}
}
